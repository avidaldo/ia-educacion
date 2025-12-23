# Diseño de Prompts

## Qué buscamos (en contexto educativo)

Un buen prompt no es “una frase ingeniosa”: es un **encargo didáctico** bien definido.

En docencia, un prompt es útil cuando ayuda a producir **materiales usables y evaluables**, por ejemplo:

- una ficha de actividad con pasos minuto a minuto,
- un banco de preguntas en un formato importable (p. ej. GIFT),
- una rúbrica con criterios observables,
- una adaptación (apoyo/ampliación) sin cambiar el objetivo.

## Plantilla base (reutilizable)

Cuando no sabes por dónde empezar, usa una plantilla. Esto funciona especialmente bien con modelos modernos.

```text
Eres un asistente de diseño didáctico para secundaria y FP.

Tarea:
- Quiero crear: [actividad / banco de preguntas / rúbrica / guía de estudio]

Contexto:
- Materia/tema:
- Nivel (curso o FP):
- Duración:
- Recursos disponibles:
- Perfil del grupo (general, sin datos personales):

Antes de responder:
- Hazme 3–5 preguntas de aclaración (solo las necesarias).
- Si falta información crítica, propón hasta 3 supuestos explícitos y continúa.

Salida:
- Formato: Markdown
- Encabezados fijos: [lista de encabezados]
- Límites: [p. ej. máx. 1 página / máx. 12 ítems / tabla]

Restricciones:
- No uses datos personales del alumnado.
- No inventes normativa, datos del centro ni cifras. Si no lo sabes, indícalo.

Criterios de calidad:
- Debe incluir criterios de éxito observables y una evaluación rápida.
```

## Técnicas fundamentales (las que más impacto tienen)

### 1) Claridad del objetivo (y evidencia)

Mal: “Haz una actividad sobre IA.”

Mejor: “Crea una actividad de 50 min para 2º FP sobre cómo **evaluar respuestas de una IA**. Evidencia: el alumnado identifica 3 errores típicos y propone 1 mejora.”

### 2) Contexto docente mínimo viable

Incluye siempre: **nivel**, **tiempo**, **recursos** y **producto final**.

Si no lo tienes claro, pide que la IA haga preguntas. Eso reduce respuestas genéricas.

### 3) Control del formato (para que sea usable)

Especifica el formato como si fuese una “plantilla de entrega”. Ejemplos útiles:

- tabla de comparación con columnas fijas,
- lista de verificación (checklist),
- Markdown con encabezados exactos.

Si vas a reutilizar el resultado en herramientas, pide formatos **estructurados** (por ejemplo JSON) *solo* cuando lo necesites.

### 4) Delimitadores (para evitar mezclas)

Si incluyes textos largos (temario, contexto, instrucciones del centro), sepáralos con delimitadores:

```text
Contexto del centro:
"""
[pega aquí el texto]
"""
```

## Prácticas “modernas” que sí se notan (calidad y rigor)

### A) Dos pasadas: borrador → auditoría → versión final

Pide primero una versión 1 y luego una auditoría contra criterios.

Ejemplo de auditoría:

```text
Revisa tu propuesta con esta lista:
1) ¿El objetivo es observable?
2) ¿Hay riesgos de privacidad?
3) ¿La evaluación mide lo que se pretende?
4) ¿Hay supuestos no declarados?

Devuelve: (a) hallazgos, (b) versión mejorada.
```

### B) Comparación A/B (cuando iteras)

En lugar de “mejóralo”, da dos versiones y pide una tabla por criterios:

```text
Compara Prompt A vs Prompt B por: claridad, formato, verificabilidad, riesgos.
Devuelve una tabla y una recomendación.
```

### C) Verificación y límites (anti-alucinaciones)

En docencia, el problema no es solo “acertar”: es **no inventar**.

Incluye restricciones como:

- “Si necesitas datos (fechas, normativa, estadísticas), indícalo y sugiere cómo verificarlo. No inventes.”
- “Marca claramente lo que sea supuesto.”

## Modelos con razonamiento (cómo pedir mejor)

Con modelos actuales, suele funcionar mejor:

- pedir una respuesta **directa**,
- pedir **supuestos** si falta información,
- y pedir una **justificación breve** basada en criterios (no un razonamiento largo).

Evita convertir el prompt en una receta interminable. Si la salida está bien especificada, el modelo “se organiza” solo.

## Cuando usar one-shot / few-shot

Úsalos sobre todo para **estilo y formato**, no para “enseñar contenido”.

- One-shot: un ejemplo de la salida deseada.
- Few-shot: 2–3 ejemplos cuando el formato es complejo o muy sensible (p. ej. rúbricas).

## Agentes y flujos (cuando el chat no basta)

Un “agente” tiene sentido cuando quieres que el sistema:

- siga un plan,
- use herramientas (p. ej., convertir a GIFT, aplicar una rúbrica, revisar formato),
- y pare cuando cumpla criterios.

Si estás diseñando un flujo, especifica:

- objetivo y criterios de parada,
- herramientas permitidas,
- restricciones (privacidad y fuentes),
- formato de salida.

## Guías oficiales recomendadas

- OpenAI: https://platform.openai.com/docs/guides/prompt-engineering
- Google Gemini: https://ai.google.dev/gemini-api/docs/prompting-intro
