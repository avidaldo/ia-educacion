---
title: Presentacións
description: Tres formas de facer presentacións con IA e como escoller entre elas, separando sempre o contido do deseño.
derived_from:
  es/webs-educativas/presentaciones.md: "8ba1f937e70def616ac39f15221015ce5d2889c5"
---

## Primeiro o contido

O erro máis común ao facer presentacións con IA é pedir de golpe «unha presentación sobre X» e quedar co que saia: diapositivas vistosas cun contido xenérico ou con erros. Funciona moito mellor en dous pasos:

1. **O contido.** Pide un esquema: título de cada diapositiva, a idea principal e o que dirás oralmente. Revísao e corríxeo como calquera outro material.
2. **O deseño.** Co esquema xa validado, xera as diapositivas coa ferramenta que prefiras.

É a mesma separación entre contido e deseño que se explica en [Técnicas avanzadas](../prompts/avanzado.md#separar-contenido-y-diseño), e a que usa esta web: as presentacións de cada módulo escríbense en texto e o estilo aplícase despois.

## Tres camiños

### Xerar a presentación nun *chatbot*

- **Gemini** crea presentacións en Canvas («crea unha presentación sobre…», a partir dun tema ou dun documento que subas) e expórtaas a Google Slides ou a PDF.
- **Os cadernos de Gemini** xeran presentacións a partir das fontes do caderno, coas súas citas; vense en [Cadernos de Gemini](../notebooks/index.md). Con contas de alumnado menor de 18 anos, esta función non está dispoñible.
- **ChatGPT e Claude** crean ficheiros de PowerPoint executando código, listos para descargar e retocar.

O mellor deste camiño é que o contido sae das túas fontes ou da conversa; o peor, que o deseño é básico e adoita requirir retoques.

### Ferramentas especializadas

Servizos como [Gamma](https://gamma.app) ou [Canva](https://www.canva.com) xeran presentacións completas, con deseño e imaxes, a partir dun texto ou dun esquema. Canva ten unha versión gratuíta para docentes e alumnado ([Canva para a educación](https://www.canva.com/education/)).

Dan o resultado máis vistoso con menos esforzo, a cambio de depender da súa plataforma, do seu plan de prezos e das súas condicións de privacidade, e dun contido que hai que revisar con máis coidado porque o deseño invita a dalo por bo.

### Texto primeiro e estilo despois

Escribir (ou pedir) a presentación en **Markdown** e convertela cunha ferramenta como [Marp](https://marp.app), [Slidev](https://sli.dev) ou [reveal.js](https://revealjs.com) en diapositivas cun estilo fixo. Pídelle ao *chatbot* o Markdown co formato da ferramenta escollida («unha diapositiva por sección, separadas por `---`»).

Require algo máis de práctica, pero o contido queda nun ficheiro de texto doado de corrixir, versionar, traducir e reutilizar, e o deseño é sempre o mesmo.

## Como escoller

| Criterio | *Chatbot* | Ferramenta especializada | Texto e estilo |
| --- | --- | --- | --- |
| Rapidez para un primeiro resultado | Alta | Moi alta | Media |
| Control do deseño | Baixo | Alto, dentro dos seus modelos | Total, unha vez definido o estilo |
| Editar despois | En PowerPoint ou Google Slides | Na súa plataforma | No texto |
| Onde quedan os teus datos | No *chatbot* | Noutra plataforma máis | Nos teus ficheiros |
| Custo | Incluído no *chatbot* | Plans gratuítos con límites | Gratuíto |

## Revisar antes de presentar

- [ ] Cada dato, data ou cita está comprobado na fonte.
- [ ] As imaxes son correctas e o seu uso está permitido (e as xeradas, indicadas como tales se procede).
- [ ] Unha idea por diapositiva e pouco texto: o demais vai no que dis ou nas notas.
- [ ] Lese ben desde o fondo da aula e no proxector real.

## Co alumnado

Unha actividade que funciona: o alumnado xera un borrador de presentación con IA, identifica que contido é correcto e cal non, corríxeo e mellora o deseño, e ao presentar explica que cambiou e por que. O que se avalía é ese proceso crítico, non o resultado visual.
