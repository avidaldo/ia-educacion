---
title: Asistentes y skills
description: Cómo fijar instrucciones y materiales para las tareas que se repiten, desde un asistente personalizado hasta una skill.
reviewed: 2026-10-22
review_every: 3
---

## Por qué fijar las instrucciones

Si generas preguntas de test cada semana, adaptas actividades a varios niveles o revisas programaciones con los mismos criterios, reescribir el *prompt* cada vez es lento y produce resultados irregulares. Todos los *chatbots* permiten **guardar las instrucciones** (y a veces materiales y procedimientos) para reutilizarlas. Hay tres niveles:

Instrucciones personalizadas
: Se aplican a **todas** tus conversaciones: quién eres, qué impartes, el tono que prefieres. Están en los ajustes de cada *chatbot*; se ven en [Chatbots](../chatbots/index.md#instrucciones-personalizadas).

Asistente personalizado
: Unas instrucciones fijas, y opcionalmente documentos, que se aplican a **las conversaciones de ese asistente**: un GPT en ChatGPT, una Gem en Gemini, un proyecto en ChatGPT o Claude, un espacio en Perplexity.

*Skill*
: Un **procedimiento** empaquetado (instrucciones, ejemplos, plantillas y, si hace falta, código) que el asistente **carga solo cuando la tarea lo requiere**, dentro de cualquier conversación.

## Asistentes personalizados

| Herramienta | Nombre | Qué incluye |
| --- | --- | --- |
| ChatGPT | GPTs | Instrucciones, ficheros de conocimiento y capacidades (búsqueda, imágenes, código). Se pueden compartir con un enlace |
| ChatGPT y Claude | Proyectos | Instrucciones y ficheros comunes a un grupo de conversaciones |
| Gemini | Gems | Instrucciones y ficheros. Disponibles también en el plan gratuito. Google las convierte en *skills* a partir de noviembre de 2026 (en las cuentas de centro, en 2027) |
| Perplexity | Espacios | Instrucciones, ficheros y búsqueda web. Se ven en [Bots educativos](../bots-educativos/index.md) |

Los nombres y lo que incluye cada plan cambian a menudo. Lo que no cambia es la idea: **un *prompt* fijo más un contexto opcional**, reutilizado en muchas conversaciones.

## *Skills*

Una *skill* es una carpeta con un fichero `SKILL.md`: un nombre, una descripción de **cuándo** usarla y las instrucciones de **cómo** hacer la tarea, más los ficheros que necesite (ejemplos, plantillas, *scripts*). La diferencia con un asistente es cómo se usa:

- El asistente solo conoce, al empezar, el nombre y la descripción de cada *skill* instalada.
- Cuando tu petición encaja con una descripción, carga esa *skill* completa y sigue su procedimiento.
- Así puede tener muchas *skills* disponibles sin llenar la conversación de instrucciones, y tú no tienes que elegir el asistente adecuado: basta con pedir la tarea.

El formato lo publicó Anthropic como estándar abierto ([Agent Skills](https://agentskills.io)) y lo han adoptado otras herramientas. En octubre de 2026:

| Dónde | Disponibilidad |
| --- | --- |
| Claude (web y aplicaciones) | Todos los planes, incluido el gratuito. Requiere activar la ejecución de código en Ajustes → Capacidades (*Capabilities*) |
| ChatGPT | Planes Business, Enterprise y Edu |
| Gemini | En despliegue desde octubre de 2026: por ahora, cuentas personales de mayores de 18 años; las cuentas de centro llegarán después. Se invocan con `/` o Gemini las aplica cuando encajan |
| Herramientas de programación con agentes (Claude Code, Codex, Gemini CLI…) | Cargan *skills* desde carpetas del proyecto |

Las *skills* pueden incluir código que el asistente ejecuta. Por eso **instala solo *skills* que hayas leído** o que vengan de una fuente de confianza: igual que una extensión del navegador, una *skill* de terceros puede contener instrucciones o código dañinos.

### Una *skill* de ejemplo

Una *skill* para generar preguntas de Moodle. La descripción es lo más importante: es lo que el asistente lee para decidir si la usa.

```markdown
---
name: preguntas-gift
description: Genera preguntas de opción múltiple en formato GIFT importable en Moodle a partir de un tema o de un material, con penalizaciones y retroalimentación. Úsala cuando pidan preguntas de test, un banco de preguntas o un examen para Moodle.
---

# Preguntas GIFT para Moodle

1. Si no se indica, pregunta el nivel del alumnado y el número de preguntas.
2. Genera cada pregunta con 4 opciones y una sola correcta; las incorrectas restan un 25 %.
3. Sigue exactamente el formato de `ejemplo.gift` (en esta misma carpeta).
4. Escapa con \ los caracteres ~ = # { } : que aparezcan en el texto.
5. Revisa antes de entregar: clave correcta, sin pistas por longitud, sin negaciones.
6. Entrega solo el contenido del fichero .gift.
```

La carpeta se completa con `ejemplo.gift`, una pregunta exportada de tu propio Moodle, como se explica en [Tests para Moodle](../tests-moodle/index.md#el-método-más-fiable-partir-de-una-exportación-de-moodle).

No hace falta escribirla a mano: Claude, ChatGPT y Gemini permiten crear una *skill* describiéndola en el chat. Describe la tarea («quiero una *skill* que genere preguntas GIFT con estas reglas…»), revisa lo que propone y pruébala con casos reales antes de usarla. Es [*metaprompting*](../prompts/index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt) aplicado a un procedimiento.

## Cómo escribir las instrucciones

Sirve para un asistente y para una *skill*:

```text
Rol y objetivo:
Eres un asistente de diseño didáctico para secundaria y FP.
Tu objetivo es [tarea concreta].

Contexto fijo:
- Nivel: [si aplica]
- Restricciones: no uses datos personales; no inventes normativa.

Formato de salida:
- [Encabezados fijos / tabla / GIFT]

Procedimiento:
1. Haz preguntas de aclaración (solo las necesarias).
2. Genera la propuesta.
3. Incluye criterios de éxito observables.
```

> [!WARNING]
> **El error más común**
> No describas el asistente («Crea un generador de preguntas de test que…»): escribe las instrucciones que debe seguir en cada conversación («Cuando el usuario te dé un tema, genera 10 preguntas en formato GIFT…»).

## Ideas para la docencia

- **Banco de preguntas**: formato GIFT o XML, criterios de calidad y un ejemplo exportado de tu Moodle.
- **Adaptador de materiales**: convierte un texto a varios niveles (apoyo y ampliación) sin perder los objetivos.
- **Revisor de actividades**: comprueba que una propuesta tiene objetivos observables, evaluación y atención a la diversidad.
- **Redactor con el estilo del departamento**: plantillas de informes, comunicaciones o programaciones con el formato del centro.
- **Corrector con rúbrica**: aplica tu rúbrica y propone una retroalimentación, que revisas tú. Nunca con datos identificativos del alumnado en una cuenta personal.

No merece la pena para tareas únicas o exploratorias (usa un chat normal) ni cuando las instrucciones cambian cada vez.

## Antes de usarlo o compartirlo

- [ ] **Objetivo claro**: ¿qué produce exactamente?
- [ ] **Formato definido**: ¿tabla, lista, GIFT, encabezados fijos?
- [ ] **Criterios de calidad**: ¿cómo sabrás que el resultado es bueno?
- [ ] **Probado**: ¿lo has usado con tres o cuatro casos reales, incluido alguno difícil?
- [ ] **Privacidad**: ¿evita pedir o guardar datos personales del alumnado?
- [ ] **Documentos revisados**: ¿los ficheros que lleva se pueden compartir con quien vaya a usarlo?
