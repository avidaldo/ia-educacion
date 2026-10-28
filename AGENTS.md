# AGENTS.md

Web y presentaciones de los cursos de inteligencia artificial para docentes de secundaria y FP (Galicia), en castellano y gallego. El [README](README.md) explica la estructura y los comandos; aquí están las reglas para escribir y mantener el contenido.

## Fuente única y flujo de trabajo

- **La web es la fuente única.** Cada módulo se escribe en castellano en `content/es/<módulo>/`. La presentación (`slides.md`) se deriva de sus páginas, y el gallego (`content/gl/`) sigue a ambos.
- **Orden de una actualización:** página en castellano → presentación en castellano (skill `update-slides`) → gallego (skill `sync-translation`). Ambas skills aplican solo lo que cambió, a partir de `uv run engine/provenance.py status` y `diff`.
- **Los hashes `derived_from` los escribe siempre el script** (`provenance.py stamp`), nunca a mano.
- **Si una presentación necesita algo que no está en la página**, se añade primero a la página: quien estudia sola solo tiene la web.
- Antes de dar algo por terminado: `uv run pytest`, `uv run engine/check.py` (0 errores) y, si cambió una presentación, `uv run engine/shoot.py --module <módulo>` (ninguna diapositiva desbordada). Si cambió una página o el tema, `uv run engine/shoot.py --audit --theme both` (cero infracciones de accesibilidad; también corre en CI).

## Público y tono

- Docentes de secundaria **y de FP**, sin formación técnica previa en IA. Se trata de entender cómo funcionan estas herramientas y de usarlas bien, no de formar especialistas.
- **Rigor y evidencia.** Los datos que caducan (modelos, planes, precios, disponibilidad, edades mínimas) se comprueban en fuentes primarias (documentación y centros de ayuda de cada proveedor) al escribir, nunca de memoria. Las páginas con esos datos llevan `reviewed:` en el *front matter*, y el comprobador avisa cuando caducan (`review_every`, en meses).
- **Las herramientas se nombran** (ChatGPT, Gemini, Claude…) y se comparan con criterios y fecha de revisión. No hay regla de neutralidad comercial.
- **Terminología precisa:** *modelo de lenguaje* para el modelo, *chatbot* para el producto, *agente* solo para sistemas que actúan con herramientas en bucle.
- **No antropomorfizar** los modelos ni presentar sus sesgos con alarmismo: se explican por su causa técnica (datos, entrenamiento, objetivo).
- Lo técnico que no todos necesitan va en bloques «Para saber más».
- **Normas:** se citan por artículo, copiando el texto oficial, y cada restricción del módulo de ética indica su origen: obligación legal, recomendación institucional o buena práctica.
- **Fuentes** como notas al pie (`[^nombre]`), con enlace y fecha de consulta cuando la página puede cambiar.

## Formato

- Markdown de `content/`, con el dialecto que documenta `engine/markdown_render.py`: alertas de GitHub (`> [!TIP]`), notas al pie, listas de tareas, contenedores de chat (`:::: chat` / `::: user` / `::: assistant`) y enlaces a la ruta del fichero fuente (`../tests-moodle/index.md#gift`), que el build convierte en URL y comprueba.
- **Nada de `style=`** ni HTML de presentación en el contenido: el estilo vive en `engine/theme/`.
- **Imágenes** en `content/assets/<módulo>/`, de menos de 300 KB y con texto alternativo; la variante gallega es un fichero hermano `nombre.gl.svg` (o `.gl.webp`).
- **Presentaciones:** solo las maquetaciones de `engine/theme/layouts.yaml` (una clase desconocida hace fallar el build), un `id` estable por diapositiva y las notas del ponente tras `Notas:`. Estilo de las presentaciones: `.claude/skills/update-slides/references/deck-style.md`.
- **Sin recursos de terceros** en la web salvo Mermaid en las páginas que lo usan.
- **No partir la prosa en líneas**: un párrafo, un elemento de lista o una fila de tabla por línea.

## Lenguas

- Castellano y gallego. Los anglicismos sin adaptar, en cursiva y con el género de su equivalente (*la skill*, *o prompt*, por decisión expresa).
- Gallego normativo (RAG). Convenciones y glosario: `.claude/skills/sync-translation/references/`. Las citas de textos oficiales solo publicados en castellano se mantienen en castellano dentro de la página gallega.

## Git

- No se hace *push* sin que lo pida quien mantiene el repositorio. Un *push* a `master` publica la web.
- No se versionan capturas con datos personales, ni la salida del build (`engine/_build/`) ni las capturas de `engine/_screens/`.
- La versión anterior de la web (Docusaurus) está en la rama `legacy-docusaurus`. Las rutas que publicaba están en `engine/legacy-urls.txt`, y `engine/redirects.yaml` dice adónde va cada una. Si se renombra o se mueve una página, o cambia un título enlazado allí con `#ancla`, se actualiza su destino en ese fichero: el *build* falla si no existe.
