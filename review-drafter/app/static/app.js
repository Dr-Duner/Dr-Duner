// Thin client: POST input -> render cards -> collect approved -> export.
const $ = (s, r = document) => r.querySelector(s);
const queue = $("#queue");
const exportBtn = $("#exportBtn");
const bulkBtn = $("#bulkBtn");
const approved = []; // {author,rating,platform,date,review,reply}
let cards = []; // {card, r, mode} for bulk approval

$("#draftBtn").addEventListener("click", async () => {
  const fd = new FormData();
  fd.append("practice", $("#practice").value);
  fd.append("pasted", $("#pasted").value);
  const f = $("#csv").files[0];
  if (f) fd.append("file", f);

  setStatus("Drafting…");
  $("#draftBtn").disabled = true;
  try {
    const res = await fetch("/api/draft", { method: "POST", body: fd });
    const data = await res.json();
    if (!res.ok) { setStatus(data.error || "Error"); return; }
    queue.innerHTML = "";
    approved.length = 0;
    cards = [];
    exportBtn.disabled = true;
    data.results.forEach(renderCard);
    const bulkable = data.results.filter(
      (d) => d.approval_mode !== "explicit").length;
    bulkBtn.disabled = bulkable === 0;
    const expl = data.results.length - bulkable;
    setStatus(`Found ${data.count} review(s) — ${bulkable} positive ` +
      `(bulk/auto), ${expl} need explicit client approval.`);
  } catch (e) {
    setStatus("Request failed.");
  } finally {
    $("#draftBtn").disabled = false;
  }
});

function setStatus(t) { $("#status").textContent = t; }

function renderCard(d) {
  const tpl = $("#cardTpl").content.cloneNode(true);
  const card = tpl.querySelector(".card");
  const r = d.review;
  if (r.is_negative) {
    card.classList.add("neg");
    tpl.querySelector(".flag").hidden = false;
  }
  tpl.querySelector(".meta").textContent =
    `${r.author || "Anonymous"} · ${r.rating ?? "—"}★ · ${r.platform}` +
    (r.date ? ` · ${r.date}` : "");
  tpl.querySelector(".text").textContent = r.text;

  const route = { explicit: "Needs explicit client approval (1–3★)",
    bulk: "Bulk-approvable (4–5★)",
    auto: "Auto-approve — practice opted in (4–5★)" }[d.approval_mode];
  const badge = document.createElement("span");
  badge.className = "chip route " + d.approval_mode;
  badge.textContent = route;
  card.classList.add("mode-" + d.approval_mode);
  tpl.querySelector(".rev").insertBefore(
    badge, tpl.querySelector(".meta"));

  const vbox = tpl.querySelector(".variants");
  d.variants.forEach((v) => {
    const el = document.createElement("div");
    el.className = "variant";
    el.innerHTML =
      `<h4>${v.label || "Variant"}</h4>
       <textarea>${escapeHtml(v.text)}</textarea>
       <p class="why${d.used_fallback ? " fallback" : ""}">
         ${d.used_fallback ? "⚠ Safe fallback template (model output could not pass the gate)" : "✓ " + escapeHtml(v.why_safe)}</p>
       <div class="vbtns">
         <button class="copy">Copy</button>
         <button class="approve ghost">Use this &amp; mark posted</button>
       </div>`;
    const ta = el.querySelector("textarea");
    el.querySelector(".copy").onclick = () => {
      navigator.clipboard.writeText(ta.value);
      flash(el.querySelector(".copy"), "Copied");
    };
    el.querySelector(".approve").onclick = () => {
      recordApproved(r, ta.value);
      finishCard(card, "posted");
    };
    vbox.appendChild(el);
  });

  tpl.querySelector(".post").onclick = () => {
    const first = card.querySelector(".variant textarea");
    recordApproved(r, first ? first.value : "");
    finishCard(card, "posted");
  };
  tpl.querySelector(".skip").onclick = () => finishCard(card, "skipped");
  queue.appendChild(tpl);
  cards.push({ card, r, mode: d.approval_mode });
}

bulkBtn.addEventListener("click", () => {
  cards.forEach(({ card, r, mode }) => {
    if (mode === "explicit" || card.classList.contains("done")) return;
    const first = card.querySelector(".variant textarea");
    recordApproved(r, first ? first.value : "");
    finishCard(card, "posted");
  });
  bulkBtn.disabled = true;
});

function recordApproved(r, reply) {
  approved.push({
    author: r.author, rating: r.rating ?? "", platform: r.platform,
    date: r.date, review: r.text, reply,
  });
  exportBtn.disabled = approved.length === 0;
}

function finishCard(card, stage) {
  card.classList.add("done");
  const chip = card.querySelector(".chip.stage");
  chip.textContent = stage;
  chip.classList.add(stage);
  card.querySelectorAll("button, textarea").forEach((b) => b.disabled = true);
}

exportBtn.addEventListener("click", async () => {
  const res = await fetch("/api/export", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ rows: approved }),
  });
  const blob = await res.blob();
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "approved_replies.csv";
  a.click();
});

function flash(btn, t) {
  const old = btn.textContent;
  btn.textContent = t;
  setTimeout(() => (btn.textContent = old), 1200);
}
function escapeHtml(s) {
  return String(s).replace(/[&<>"]/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}
