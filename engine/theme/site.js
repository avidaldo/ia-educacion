// Web behaviour: theme toggle, mobile navigation, copy buttons, embedded decks, Mermaid and the active TOC entry.

const root = document.documentElement;

document.querySelector(".theme-toggle")?.addEventListener("click", () => {
  const next = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = next;
  localStorage.setItem("ia-edu-theme", next);
  renderMermaid();
});

const navToggle = document.querySelector(".nav-toggle");
navToggle?.addEventListener("click", () => {
  const open = document.body.classList.toggle("nav-open");
  navToggle.setAttribute("aria-expanded", String(open));
});

const labels = { copy: document.body.dataset.copyLabel, copied: document.body.dataset.copiedLabel };

function addCopyButton(container, getText) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "copy-button";
  button.textContent = labels.copy;
  button.addEventListener("click", async () => {
    await navigator.clipboard.writeText(getText());
    button.textContent = labels.copied;
    setTimeout(() => { button.textContent = labels.copy; }, 1500);
  });
  container.append(button);
}

document.querySelectorAll(".code-block").forEach((block) => {
  addCopyButton(block, () => block.querySelector("pre").innerText);
});
document.querySelectorAll(".chat-user").forEach((message) => {
  addCopyButton(message, () => message.querySelector(".chat-body").innerText);
});

document.querySelectorAll(".deck-card").forEach((card) => {
  card.querySelector(".deck-load")?.addEventListener("click", (event) => {
    const frame = card.querySelector(".deck-frame");
    if (!frame.querySelector("iframe")) {
      const iframe = document.createElement("iframe");
      iframe.src = card.dataset.deckUrl;
      iframe.title = card.querySelector(".deck-card-title").textContent;
      iframe.loading = "lazy";
      iframe.allowFullscreen = true;
      frame.append(iframe);
    }
    frame.hidden = !frame.hidden;
    event.currentTarget.setAttribute("aria-expanded", String(!frame.hidden));
  });
});

const mermaidSources = new Map();
async function renderMermaid() {
  const mermaid = window.iaEduMermaid;
  const blocks = document.querySelectorAll("pre.mermaid");
  if (!mermaid || blocks.length === 0) return;
  blocks.forEach((block) => {
    if (!mermaidSources.has(block)) mermaidSources.set(block, block.textContent);
    block.removeAttribute("data-processed");
    block.textContent = mermaidSources.get(block);
  });
  // "base" is the only Mermaid theme that takes variables; they come from tokens.css so diagrams follow both themes.
  const token = (name) => getComputedStyle(root).getPropertyValue(name).trim();
  mermaid.initialize({
    startOnLoad: false,
    theme: "base",
    themeVariables: {
      darkMode: root.dataset.theme === "dark",
      fontFamily: token("--font-sans"),
      background: token("--bg"),
      primaryColor: token("--accent-soft"),
      primaryBorderColor: token("--accent"),
      primaryTextColor: token("--ink"),
      lineColor: token("--ink-2"),
      textColor: token("--ink"),
    },
  });
  await mermaid.run({ nodes: blocks });
}
document.addEventListener("ia-edu:mermaid-ready", renderMermaid);
if (window.iaEduMermaid) renderMermaid();

const tocLinks = [...document.querySelectorAll(".toc a")];
if (tocLinks.length && "IntersectionObserver" in window) {
  const byId = new Map(tocLinks.map((link) => [decodeURIComponent(link.hash.slice(1)), link]));
  const observer = new IntersectionObserver((entries) => {
    entries.filter((entry) => entry.isIntersecting).forEach((entry) => {
      tocLinks.forEach((link) => link.classList.remove("active"));
      byId.get(entry.target.id)?.classList.add("active");
    });
  }, { rootMargin: "0px 0px -70% 0px" });
  byId.forEach((_, id) => { const heading = document.getElementById(id); if (heading) observer.observe(heading); });
}
