"""FastAPI app: one page, three endpoints. Keep routes thin."""
from __future__ import annotations

import csv
import io

from fastapi import FastAPI, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import (approvals, channels, config, drafter, google_gbp, models,
               parser, practices, store)

app = FastAPI(title="Review Response Drafter")
app.mount("/static", StaticFiles(directory=config.ROOT / "app" / "static"),
          name="static")
templates = Jinja2Templates(directory=config.ROOT / "app" / "templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {
        "practices": practices.list_practices(),
        "has_api_key": config.has_api_key(),
    })


@app.post("/api/draft")
async def api_draft(
    practice: str = Form("default"),
    pasted: str = Form(""),
    file: UploadFile | None = None,
):
    if file is not None and file.filename:
        raw = (await file.read()).decode("utf-8", errors="replace")
        reviews = parser.parse(raw, is_csv=True)
    else:
        reviews = parser.parse(pasted, is_csv=False)

    if not reviews:
        return JSONResponse({"error": "No reviews found in input."},
                            status_code=400)

    cfg = practices.load_practice(practice)
    drafted = drafter.draft_all(reviews, cfg)
    return JSONResponse({
        "count": len(reviews),
        "results": [d.to_dict() for d in drafted],
    })


@app.post("/api/approvals")
async def api_approvals(request: Request):
    """Operator pushes a drafted batch into the client approval queue
    and we deliver it on the practice's channel. Returns the exact
    message the client will receive (operator can preview/confirm)."""
    body = await request.json()
    name = body.get("practice", "default")
    cfg = practices.load_practice(name)
    drafted: list[models.DraftedReview] = []
    for row in body.get("items", []):
        rv = models.Review(
            text=row.get("review", ""), author=row.get("author", ""),
            rating=row.get("rating") or None,
            platform=row.get("platform", "google"),
            date=row.get("date", ""))
        var = models.DraftVariant(text=row.get("reply", ""),
                                  why_safe=row.get("why_safe", ""),
                                  label="approved")
        drafted.append(models.DraftedReview(
            review=rv, variants=[var],
            approval_mode=models.approval_mode(rv, cfg)))
    items = approvals.create_from_drafted(name, cfg, drafted)
    pending = [i for i in items if i.status == store.PENDING
               or i.status == store.APPROVED]
    delivery = channels.get_sender(cfg).send(
        cfg, [i for i in items if i.status == store.PENDING]) \
        if any(i.status == store.PENDING for i in items) \
        else {"sent": 0, "channel": cfg.approval_channel}
    return JSONResponse({
        "queued": len(items),
        "auto_approved": sum(i.status == store.APPROVED for i in items),
        "channel": cfg.approval_channel,
        "delivery": delivery,
        "approve_url": f"/approve/{pending[0].token}" if pending else None,
    })


@app.get("/api/queue/{practice}")
def api_queue(practice: str):
    return JSONResponse({"items": [
        {"id": i.id, "status": i.status, "mode": i.approval_mode,
         "rating": i.review.get("rating"),
         "author": i.review.get("author"), "reply": i.reply}
        for i in store.list_items(practice)]})


@app.post("/api/post/{practice}")
def api_post(practice: str):
    """Simulated Google post-back of approved replies. Real Google is
    credential-gated; this proves the pipeline offline."""
    return JSONResponse(approvals.post_approved(practice))


@app.get("/approve/{token}", response_class=HTMLResponse)
def approve_page(request: Request, token: str):
    found = store.find_by_token(token)
    if not found:
        return HTMLResponse("<h1>Link expired or invalid.</h1>",
                            status_code=404)
    name, _ = found
    cfg = practices.load_practice(name)
    pending = store.list_items(name, store.PENDING)
    payload = channels.render_link_payload(cfg, pending)
    return templates.TemplateResponse(request, "approve.html", {
        "token": token, "practice": payload["practice_name"],
        "positives": payload["positives"], "explicit": payload["explicit"],
    })


@app.post("/approve/{token}")
async def approve_action(request: Request, token: str):
    body = await request.json()
    action = body.get("action", "")
    if action == "approve_all_positives":
        found = store.find_by_token(token)
        if not found:
            return JSONResponse({"ok": False, "error": "invalid link"},
                                status_code=404)
        return JSONResponse(approvals.bulk_approve_positives(found[0]))
    return JSONResponse(approvals.apply_action(
        token, action, item_id=body.get("item"),
        edited_text=body.get("text")))


@app.post("/api/export")
async def api_export(request: Request):
    rows = (await request.json()).get("rows", [])
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["author", "rating", "platform", "date",
                "review", "approved_reply"])
    for r in rows:
        w.writerow([r.get("author", ""), r.get("rating", ""),
                    r.get("platform", ""), r.get("date", ""),
                    r.get("review", ""), r.get("reply", "")])
    buf.seek(0)
    return StreamingResponse(
        iter([buf.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition":
                 "attachment; filename=approved_replies.csv"},
    )
