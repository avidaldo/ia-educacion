---
title: Ejemplos comentados
description: Conversaciones reales que muestran cada técnica, con el porqué de que funcionen.
reviewed: 2026-10-28
---

La idea no es copiar el contenido que genera la IA, sino **aprender a pedirlo**: con contexto, restricciones y verificación.

## Un *prompt* que escribe *prompts*

Este es un caso de [*metaprompting*](index.md#metaprompting-pedirle-a-la-ia-que-escriba-el-prompt): en lugar de pedir una actividad, se pide la plantilla que servirá para pedir cualquier actividad.

:::: chat
::: user
Actúa como un asesor pedagógico especializado en secundaria y FP.

Objetivo: necesito un prompt reutilizable para pedir a una IA que genere una actividad de aula (45-60 min) sobre cualquier tema.

Requisitos del prompt:

- Debe empezar pidiendo 3-5 preguntas de aclaración (nivel, materia, requisitos del centro, tiempo, recursos).
- Debe producir una ficha lista para usar con: objetivos, criterios de éxito, materiales, pasos minuto a minuto, atención a la diversidad (2 adaptaciones), y evaluación rápida (*exit ticket*).
- Debe evitar inventar normativa o «datos del centro»; si falta información debe marcarlo como supuesto.
- Debe pedir el formato de salida en Markdown con encabezados fijos.

Devuélveme SOLO el prompt final (en español).
:::
::: assistant collapsed
Copia y pega este prompt (es un «prompt plantilla»):

```text
Eres un asistente de diseño didáctico para secundaria y FP. Tu objetivo es ayudarme a crear una actividad de aula lista para usar.

1) Antes de proponer la actividad, hazme 3–5 preguntas de aclaración (solo las necesarias) sobre:
- Materia/tema y curso o nivel
- Tiempo disponible (45–60 min)
- Recursos (aula, proyector, móviles, internet, etc.)
- Perfil del grupo (heterogeneidad, NEAE, nivel lingüístico)
- Criterios o evidencias de aprendizaje que quiero observar

2) Si falta información crítica, propón supuestos explícitos (máximo 3) y continúa.

3) Genera una ficha de actividad en Markdown con estos encabezados EXACTOS:
- Objetivo
- Objetivos de aprendizaje (3–5)
- Criterios de éxito (observables)
- Materiales
- Desarrollo (minuto a minuto)
- Atención a la diversidad (2 adaptaciones: apoyo y ampliación)
- Evaluación rápida (exit ticket de 3 ítems)
- Riesgos y cómo mitigarlos

4) Restricciones:
- No inventes normativa, datos del centro ni cifras. Si algo no está en el contexto, indícalo como supuesto.
- Evita jerga innecesaria; escribe para un docente principiante/intermedio.

Tema: [escribe aquí el tema]
```
:::
::::

> [!TIP]
> **Por qué funciona**
> - Define el rol (asesoría pedagógica) y el **objetivo** (una actividad lista para usar).
> - Obliga a hacer **preguntas de aclaración** antes de escribir la propuesta.
> - Controla la salida con **encabezados fijos** y restricciones (no inventar datos, marcar supuestos).
> - Introduce una buena práctica de **privacidad**: no usar datos del centro ni del alumnado.

## Dar un ejemplo de salida (*one-shot*)

:::: chat
::: user
Quiero un ejemplo de salida para una «ficha de actividad» que yo pueda usar como patrón.

Ejemplo (patrón de formato) para una actividad cualquiera:

- Título: ...
- Objetivo: ...
- Desarrollo: 3 pasos numerados
- Evaluación: 2 criterios

Ahora crea UNA ficha nueva sobre «cómo enseñar a mi alumnado a escribir buenos prompts», para 4.º ESO o 1.º FP Básica. Reglas:

- Máximo 180 palabras.
- Respeta el mismo patrón de formato.
:::
::: assistant
- Título: Taller exprés: «Preguntar bien a una IA»
- Objetivo: Que el alumnado convierta una petición vaga en un prompt claro con contexto, restricciones y formato.
- Desarrollo:
  1. (10 min) En parejas, reescriben «Explícame X» añadiendo: público, longitud y formato.
  2. (20 min) Comparan dos prompts sobre el mismo tema y eligen cuál es más verificable.
  3. (15 min) Crean su propio prompt para generar una ficha de estudio y lo prueban.
- Evaluación:
  - El prompt incluye contexto (nivel, tema, objetivo) y restricciones (longitud/formato).
  - La salida es evaluable (tiene criterios de éxito o una lista de comprobación).
:::
::::

## Dar varios ejemplos (*few-shot*)

:::: chat
::: user
Estoy creando un asistente para docentes. Necesito que la IA genere «instrucciones para una tarea» con un estilo consistente.

Aquí tienes DOS ejemplos del estilo exacto que quiero (formato y tono):

Ejemplo 1
Tarea: Resume un texto.
Entrega: 8-10 líneas.
Criterios: incluye idea central + 3 ideas clave + 1 duda.

Ejemplo 2
Tarea: Debate guiado.
Entrega: 1 postura + 2 argumentos + 1 contraargumento.
Criterios: argumentos basados en evidencias del material.

Ahora genera 3 instrucciones de tarea nuevas para «aprender a usar IA de forma responsable en clase». Reglas:

- Mantén EXACTAMENTE el mismo patrón de 3 líneas (Tarea / Entrega / Criterios).
- Nivel: 2.º FP Grado Medio.
:::
::: assistant
Tarea: Auditoría de una respuesta de IA.
Entrega: 6-8 líneas con 3 riesgos y 3 mitigaciones.
Criterios: menciona privacidad, sesgos y verificación.

Tarea: Diseña un prompt seguro.
Entrega: 1 prompt con contexto + 3 restricciones + formato de salida.
Criterios: evita datos personales y exige evidencias.

Tarea: Checklist de uso responsable.
Entrega: lista de 7 ítems «antes/durante/después».
Criterios: ítems accionables y verificables.
:::
::::

> [!TIP]
> **Por qué funciona**
> - Los ejemplos fijan un patrón de salida estable.
> - Controla el **formato** (tres líneas fijas) y el **nivel**.
> - Reduce la ambigüedad: el resultado se puede evaluar.

## Pedir una crítica del propio *prompt*

Pedir explícitamente que se señale todo lo cuestionable evita la tendencia de los *chatbots* a darte la razón, y obliga a un análisis con criterios.

:::: chat
::: user
Haz un análisis exhaustivo señalando todo aquello que pueda ser cuestionable, incompleto o mejorable en el siguiente prompt.

Quiero que lo evalúes críticamente con mentalidad de docente: detecta ambigüedades, posibles sesgos (p. ej. ejemplos estereotipados), riesgos de privacidad, y falta de verificabilidad. Luego propón una versión mejor.

Prompt: «Crea una actividad divertida sobre IA para mi clase y pon ejemplos reales de mis alumnos.»
:::
::: assistant collapsed
**Análisis crítico del prompt**

1. **Ambigüedad.** «Actividad divertida» no define objetivos, duración, nivel ni producto final. «Sobre IA» es demasiado amplio: ¿uso responsable, conceptos, herramientas, ética, sesgos, evaluación de respuestas?
2. **Riesgos de privacidad.** «Ejemplos reales de mis alumnos» puede implicar datos personales o situaciones identificables. Es un riesgo claro y evitable.
3. **Sesgos y estereotipos.** Sin restricciones, el modelo puede usar ejemplos «típicos» con sesgos (género, origen, etc.) o situaciones sensibles.
4. **Falta de verificabilidad.** No hay criterios de éxito ni evaluación, y sin formato la respuesta puede ser difícil de usar.

**Versión mejorada**

```text
Eres un asistente de diseño didáctico para secundaria/FP.

Antes de proponer nada, hazme 4 preguntas de aclaración sobre: nivel, tema exacto (uso responsable / evaluación de respuestas / sesgos), tiempo y recursos.

Requisitos:
- NO uses datos personales ni ejemplos basados en alumnado real. Usa ejemplos ficticios y neutrales.
- Incluye: objetivos (3), criterios de éxito, materiales, desarrollo minuto a minuto, 2 adaptaciones (apoyo y ampliación) y un exit ticket de 3 ítems.
- Formato: Markdown con encabezados fijos.

Contexto inicial: [describe aquí tu grupo en términos generales, sin datos personales].
```
:::
::::

## Comparar dos *prompts* en una tabla

Cuando dudas entre dos versiones, una comparación por criterios da un *feedback* más concreto que «¿cuál es mejor?».

:::: chat
::: user
Soy docente y tengo dos versiones de un prompt para generar una ficha de actividad. Quiero que compares ambos y me digas cuál es mejor y por qué, en una tabla.

Columnas: «Criterio», «Prompt A», «Prompt B», «Recomendación». Criterios mínimos: claridad del objetivo, información faltante, control del formato, verificabilidad, y riesgos (sesgos/privacidad).

Prompt A: «Hazme una actividad sobre inteligencia artificial para mis alumnos.»

Prompt B: «Crea una actividad de 50 min para 2.º FP sobre cómo evaluar respuestas de una IA. Incluye objetivos, materiales, pasos minuto a minuto, 2 adaptaciones y un exit ticket. No inventes normativa ni datos. Formato Markdown con encabezados.»
:::
::: assistant collapsed
| Criterio | Prompt A | Prompt B | Recomendación |
| --- | --- | --- | --- |
| Claridad del objetivo | Vago: no indica qué se quiere conseguir (aprendizaje, producto, duración). | Claro: define tema concreto (evaluar respuestas de IA) y duración. | Mantén un objetivo observable («el alumnado detecta 3 errores típicos…»). |
| Información faltante | No pide contexto (nivel, recursos, tiempo, perfil). | Incluye nivel y tiempo; faltan recursos y perfil del grupo. | Añade 3–5 preguntas de aclaración antes de generar la actividad. |
| Control del formato | Sin formato: salida impredecible. | Pide Markdown con encabezados. | Especifica encabezados fijos y límites (p. ej., «máx. 1 página»). |
| Verificabilidad | Difícil evaluar si «sirve». | Incluye *exit ticket* y estructura; más evaluable. | Añade criterios de éxito y evidencias de aprendizaje. |
| Riesgos | No menciona riesgos: puede introducir ejemplos problemáticos o pedir datos personales. | Menciona no inventar normativa; no trata privacidad. | Añade: «no uses datos personales; incluye advertencias de sesgo y verificación». |

Mejor prompt: **B**, porque reduce ambigüedad y controla la salida. Aun así, lo mejoraría pidiendo aclaraciones y añadiendo privacidad y verificación.
:::
::::

> [!TIP]
> **Por qué funciona**
> - Convierte una opinión en una revisión **estructurada**.
> - Obliga a hablar de formato, verificabilidad y riesgos.
> - La recomendación final sale de criterios, no de preferencias de estilo.
