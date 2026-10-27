// Composes the session deck from ?m=module,module before starting reveal.js; shows the module picker without ?m=.

const body = document.body;
const vendorUrl = body.dataset.vendorUrl;
const data = JSON.parse(document.getElementById("deck-data").textContent);
const params = new URLSearchParams(location.search);
const inFrame = params.get("frame") === "1";
const knownModules = new Map(data.modules.map((module) => [module.slug, module]));
const requestedValue = params.get("m");

if (params.get("theme") === "dark") document.documentElement.dataset.theme = "dark";

if (requestedValue === null) {
  showPicker();
} else {
  const requested = requestedValue === "all" || requestedValue === ""
    ? data.modules.map((module) => module.slug)
    : requestedValue.split(",").map((slug) => slug.trim()).filter((slug) => knownModules.has(slug));
  composeDeck(requested);
  await startReveal();
}

function composeDeck(selected) {
  const slides = document.querySelector(".reveal .slides");
  const sections = [...slides.children];
  const sectionsOf = (module) => sections.filter((section) => section.dataset.module === module);
  const ordered = [];
  const withFrame = !inFrame;
  if (withFrame) ordered.push(...sectionsOf("_cover"));
  if (withFrame && selected.length > 1) {
    const agenda = sectionsOf("_agenda")[0];
    const list = agenda.querySelector(".agenda-list");
    for (const slug of selected) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = `#/${slug}--inicio`;
      link.textContent = knownModules.get(slug).title;
      item.append(link);
      list.append(item);
    }
    ordered.push(agenda);
  }
  for (const slug of selected) ordered.push(...sectionsOf(slug));
  if (withFrame) ordered.push(...sectionsOf("_closing"));
  slides.replaceChildren(...ordered);
}

async function startReveal() {
  const { default: Reveal } = await import(`${vendorUrl}reveal.mjs`);
  const { default: RevealNotes } = await import(`${vendorUrl}plugin/notes.mjs`);
  await Reveal.initialize({
    width: data.width,
    height: data.height,
    margin: 0,
    center: false,
    hash: !inFrame,
    respondToHashChanges: !inFrame,
    controls: true,
    progress: true,
    slideNumber: "c/t",
    transition: "fade",
    transitionSpeed: "fast",
    backgroundTransition: "none",
    scrollActivationWidth: inFrame ? null : 435,
    plugins: [RevealNotes],
  });
  const deck = Reveal;
  window.Reveal = Reveal;
  if (document.querySelector(".reveal pre.mermaid")) {
    const { default: mermaid } = await import(body.dataset.mermaidUrl);
    mermaid.initialize({ startOnLoad: false, theme: "neutral" });
    const renderCurrent = () => {
      const pending = deck.getCurrentSlide().querySelectorAll("pre.mermaid:not([data-processed])");
      if (pending.length) mermaid.run({ nodes: pending });
    };
    deck.on("slidechanged", renderCurrent);
    renderCurrent();
  }
}

function showPicker() {
  const picker = document.querySelector(".deck-picker");
  const start = picker.querySelector(".deck-picker-start");
  document.querySelector(".reveal").hidden = true;
  picker.hidden = false;
  const chosen = [];
  const refresh = () => {
    picker.querySelectorAll("input[type=checkbox]").forEach((input) => {
      const position = chosen.indexOf(input.value);
      input.closest("label").querySelector(".order").textContent = position >= 0 ? `${position + 1}.` : "";
    });
    start.href = `?m=${chosen.join(",")}`;
    start.setAttribute("aria-disabled", String(chosen.length === 0));
  };
  picker.addEventListener("change", (event) => {
    const { value, checked } = event.target;
    const position = chosen.indexOf(value);
    if (checked && position < 0) chosen.push(value);
    if (!checked && position >= 0) chosen.splice(position, 1);
    refresh();
  });
  refresh();
}
