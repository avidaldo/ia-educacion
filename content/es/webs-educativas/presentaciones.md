---
title: Presentaciones
description: Tres formas de hacer presentaciones con IA y cómo elegir entre ellas, separando siempre el contenido del diseño.
reviewed: 2026-10-22
review_every: 3
---

## Primero el contenido

El error más común al hacer presentaciones con IA es pedir de golpe «una presentación sobre X» y quedarse con lo que salga: diapositivas vistosas con un contenido genérico o con errores. Funciona mucho mejor en dos pasos:

1. **El contenido.** Pide un esquema: título de cada diapositiva, la idea principal y lo que dirás oralmente. Revísalo y corrígelo como cualquier otro material.
2. **El diseño.** Con el esquema ya validado, genera las diapositivas con la herramienta que prefieras.

Es la misma separación entre contenido y diseño que se explica en [Técnicas avanzadas](../prompts/avanzado.md#separar-contenido-y-diseño), y la que usa esta web: las presentaciones de cada módulo se escriben en texto y el estilo se aplica después.

## Tres caminos

### Generar la presentación en un *chatbot*

- **Gemini** crea presentaciones en Canvas («crea una presentación sobre…», a partir de un tema o de un documento que subas) y las exporta a Google Slides o a PDF.
- **Los cuadernos de Gemini** generan presentaciones a partir de las fuentes del cuaderno, con sus citas; se ven en [Cuadernos de Gemini](../notebooks/index.md). Con cuentas de alumnado menor de 18 años, esta función no está disponible.
- **ChatGPT y Claude** crean ficheros de PowerPoint ejecutando código, listos para descargar y retocar.

Lo mejor de este camino es que el contenido sale de tus fuentes o de la conversación; lo peor, que el diseño es básico y suele requerir retoques.

### Herramientas especializadas

Servicios como [Gamma](https://gamma.app) o [Canva](https://www.canva.com) generan presentaciones completas, con diseño e imágenes, a partir de un texto o un esquema. Canva tiene una versión gratuita para docentes y alumnado ([Canva para la educación](https://www.canva.com/education/)).

Dan el resultado más vistoso con menos esfuerzo, a cambio de depender de su plataforma, de su plan de precios y de sus condiciones de privacidad, y de un contenido que hay que revisar con más cuidado porque el diseño invita a darlo por bueno.

### Texto primero y estilo después

Escribir (o pedir) la presentación en **Markdown** y convertirla con una herramienta como [Marp](https://marp.app), [Slidev](https://sli.dev) o [reveal.js](https://revealjs.com) en diapositivas con un estilo fijo. Pide al *chatbot* el Markdown con el formato de la herramienta elegida («una diapositiva por sección, separadas por `---`»).

Requiere algo más de práctica, pero el contenido queda en un fichero de texto fácil de corregir, versionar, traducir y reutilizar, y el diseño es siempre el mismo.

## Cómo elegir

| Criterio | *Chatbot* | Herramienta especializada | Texto y estilo |
| --- | --- | --- | --- |
| Rapidez para un primer resultado | Alta | Muy alta | Media |
| Control del diseño | Bajo | Alto, dentro de sus plantillas | Total, una vez definido el estilo |
| Editar después | En PowerPoint o Google Slides | En su plataforma | En el texto |
| Dónde quedan tus datos | En el *chatbot* | En otra plataforma más | En tus ficheros |
| Coste | Incluido en el *chatbot* | Planes gratuitos con límites | Gratuito |

## Revisar antes de presentar

- [ ] Cada dato, fecha o cita está comprobado en la fuente.
- [ ] Las imágenes son correctas y su uso está permitido (y las generadas, indicadas como tales si procede).
- [ ] Una idea por diapositiva y poco texto: lo demás va en lo que dices o en las notas.
- [ ] Se lee bien desde el fondo del aula y en el proyector real.

## Con el alumnado

Una actividad que funciona: el alumnado genera un borrador de presentación con IA, identifica qué contenido es correcto y qué no, lo corrige y mejora el diseño, y al presentar explica qué cambió y por qué. Lo que se evalúa es ese proceso crítico, no el resultado visual.
