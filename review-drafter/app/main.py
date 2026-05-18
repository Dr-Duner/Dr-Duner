"""FastAPI app: one page, three endpoints. Keep routes thin."""
from __future__ import annotations

import csv
import io

from fastapi import FastAPI, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import config, drafter, parser, practices

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
