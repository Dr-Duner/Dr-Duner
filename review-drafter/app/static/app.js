// Operator console: draft -> QA (pick/edit a variant) -> send for
// client approval -> post approved. The operator never self-approves;
// the client approves on their channel. Thin client over the API.
const $ = (s, r = document) => r.querySelector(s);
const queue = $("#queue");
const sendBtn = $("#sendBtn");
const postBtn = $("#postBtn");
const queueBtn = $("#queueBtn");
const sendOut = $("#sendOut");
let cards = []; // {card, r} — the QA'd batch

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
    cards = [];
    $("#dispatch").hidden = true;
    data.results.forEach(renderCard);
    const bulkable = data.results.filter(
      (d) => d.approval_mode !== "explicit").length;
    sendBtn.disabled = data.results.length === 0;
    postBtn.disabled = true;
    queueBtn.disabled = false;
    const expl = data.results.length - bulkable;
    setStatus(`Found ${data.count} review(s) — ${bulkable} positive ` +
      `(bulk/auto), ${expl} need explicit client approval. ` +
      `Pick/edit a reply per card, then Send.`);
  } catch (e) {
    setStatus("Request failed.");
  } finally {
    $("#draftBtn").disabled = false;
  }
});

function setStatus(t) { $("#status").textContent = t; }

const ROUTE = {
  explicit: "Needs explicit client approval (1–3★)",
  bulk: "Bulk-approvable (4–5★)",
  auto: "Auto-approve — practice opted in (4–5★)",
};

function renderCard(d) {
  const tpl = $("#cardTpl").content.cloneNode(true);
  const card = tpl.querySelector(".card");
  const r = d.review;
  if (r.is_negative) card.classList.add("neg");
  card.classList.add("mode-" + d.approval_mode);

  const badge = document.createElement("span");
  badge.className = "chip route " + d.approval_mode;
  badge.textContent = ROUTE[d.approval_mode];
  tpl.querySelector(".rev").insertBefore(badge, tpl.querySelector(".meta"));

  tpl.querySelector(".meta").textContent =
    `${r.author || "Anonymous"} · ${r.rating ?? "—"}★ · ${r.platform}` +
    (r.date ? ` · ${r.date}` : "");
  tpl.querySelector(".text").textContent = r.text;

  const vbox = tpl.querySelector(".variants");
  const gname = "v" + cards.length;
  d.variants.forEach((v, i) => {
    const el = document.createElement("div");
    el.className = "variant";
    el.innerHTML =
      `<label class="vpick"><input type="radio" name="${gname}"
        ${i === 0 ? "checked" : ""}> <strong>${v.label || "Variant"}</strong></label>
       <textarea>${escapeHtml(v.text)}</textarea>
       <p class="why${d.used_fallback ? " fallback" : ""}">
         ${d.used_fallback
            ? "⚠ Safe fallback template (model output could not pass the gate)"
            : "✓ " + escapeHtml(v.why_safe)}</p>
       <button class="copy ghost">Copy</button>`;
    const ta = el.querySelector("textarea");
    el.querySelector(".copy").onclick = () => {
      navigator.clipboard.writeText(ta.value);
      flash(el.querySelector(".copy"), "Copied");
    };
    vbox.appendChild(el);
  });

  queue.appendChild(tpl);
  cards.push({ card, r });
}

function chosen(card) {
  const variants = [...card.querySelectorAll(".variant")];
  const picked = variants.find(
    (v) => v.querySelector('input[type=radio]').checked) || variants[0];
  return {
    text: picked.querySelector("textarea").value,
    why: picked.querySelector(".why").textContent.replace(/^[✓⚠]\s*/, "").trim(),
  };
}

function currentItems() {
  return cards.map(({ card, r }) => {
    const c = chosen(card);
    return {
      author: r.author, rating: r.rating ?? null,
      platform: r.platform || "google", date: r.date, review: r.text,
      reply: c.text, why_safe: c.why,
    };
  });
}

sendBtn.addEventListener("click", async () => {
  sendBtn.disabled = true;
  $("#dispatch").hidden = false;
  sendOut.textContent = "Sending for client approval…";
  const practice = $("#practice").value;
  try {
    const res = await fetch("/api/approvals", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ practice, items: currentItems() }),
    });
    const j = await res.json();
    sendOut.textContent =
      `Queued ${j.queued} — ${j.auto_approved} auto-approved, ` +
      `delivered via ${j.channel} to ${j.delivery.to || "outbox"}.`;
    if (j.approve_url) {
      const url = location.origin + j.approve_url;
      const a = $("#clientHref");
      a.href = url; a.textContent = url;
      $("#clientLink").hidden = false;
      $("#copyLink").onclick = () => {
        navigator.clipboard.writeText(url);
        flash($("#copyLink"), "Copied");
      };
    }
    const prev = j.delivery && j.delivery.preview;
    if (prev) {
      $("#preview").textContent =
        typeof prev === "string" ? prev
          : (prev.text || JSON.stringify(prev, null, 2));
      $("#previewBox").hidden = false;
    }
    postBtn.disabled = false;
  } catch (e) {
    sendOut.textContent = "Send failed.";
    sendBtn.disabled = false;
  }
});

postBtn.addEventListener("click", async () => {
  postBtn.disabled = true;
  const practice = $("#practice").value;
  const res = await fetch("/api/post/" + encodeURIComponent(practice),
    { method: "POST" });
  const j = await res.json();
  sendOut.textContent =
    `Posted ${j.posted} approved reply(ies)` +
    (j.live ? " (LIVE Google)." : " (simulated — Google access pending).") +
    (j.blocked && j.blocked.length
      ? ` ${j.blocked.length} blocked by final HIPAA scan.` : "");
  refreshQueue();
});

queueBtn.addEventListener("click", refreshQueue);

async function refreshQueue() {
  const practice = $("#practice").value;
  const res = await fetch("/api/queue/" + encodeURIComponent(practice));
  const j = await res.json();
  const by = {};
  j.items.forEach((i) => (by[i.status] = (by[i.status] || 0) + 1));
  const order = ["pending", "approved", "posted", "rejected"];
  $("#dispatch").hidden = false;
  $("#queueOut").textContent = "Queue: " +
    (order.filter((s) => by[s]).map((s) => `${by[s]} ${s}`).join(" · ")
      || "empty");
}

function flash(btn, t) {
  const old = btn.textContent;
  btn.textContent = t;
  setTimeout(() => (btn.textContent = old), 1200);
}
function escapeHtml(s) {
  return String(s).replace(/[&<>"]/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}
