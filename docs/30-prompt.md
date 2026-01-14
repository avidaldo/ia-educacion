# Diseño de Prompts

## Definición y Propósito

Un prompt eficaz funciona como una **especificación técnica** precisa.

En el contexto educativo, el diseño de prompts debe orientarse a la producción de **artefactos funcionales y verificables**, tales como:

- Fichas de actividad con desgloses temporales detallados.
- Bancos de preguntas en formatos estándar de importación (ej. GIFT).
- Rúbricas de evaluación con indicadores observables.
- Adaptaciones curriculares que mantengan la alineación con los objetivos de aprendizaje.

## Estructura de Referencia (Ejemplo)

La siguiente estructura sirve como punto de partida para diseñar prompts robustos, facilitando la interacción con modelos de lenguaje avanzados.

```text
Eres un consultor experto en diseño curricular y normativa educativa.

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

### 1) Definición de Rol (Persona Pattern)

Asignar un rol no sirve para hacer al modelo "más listo", sino para **comprimir instrucciones**: activa sus *priors* (conocimientos y tonos pre-asociados) para alinear la respuesta con una expectativa específica, descartando vocabulario o estilos irrelevantes. Es útil para establecer el **estilo* con el queremos la respuesta, pero no es necesario si la definición del resultado que queremos es suficientemente detallada.

- **Mal uso (Lazy Prompting):** "Eres un experto en Python."
  - *Problema:* Delegas en el modelo la definición de "experto". Puede activar *priors* indeseados (ej. usar librerías obsoletas) si no especificas más.

- **Buen uso (Filtro de Enfoque):** "Actúa como un Auditor de Seguridad (Senior): revisa este código buscando vulnerabilidades críticas (OWASP Top 10) y sugiere correcciones defensivas."
  - *Ventaja:* Usas el rol para establecer la "lente" (perspectiva crítica) y las instrucciones para definir la "tarea" (criterios OWASP).

El rol configura el *quién* (la voz), pero nunca debe sustituir al *qué* (las instrucciones). Si confías solo en el rol para tareas lógicas o factuales, aumentas el riesgo de alucinaciones plausibles.

### 2) Claridad del objetivo (y evidencia)

Mal: “Haz una actividad sobre IA.”

Mejor: “Crea una actividad de 50 min para 2º FP sobre cómo **evaluar respuestas de una IA**. Evidencia: el alumnado identifica 3 errores típicos y propone 1 mejora.”

### 3) Contexto docente mínimo viable

Incluye siempre: **nivel**, **tiempo**, **recursos** y **producto final**. Proporcionar estos datos reduce drásticamente las respuestas genéricas.

### 4) Interacción Inversa (Flipped Interaction)

Consiste en pedir al modelo que te entreviste antes de generar la respuesta final.

- **En la plantilla:** "Hazme 3–5 preguntas de aclaración (solo las necesarias)".
- **Por qué funciona:** Obliga al modelo a detectar lagunas en tu petición antes de "alucinar" detalles (ej. asumir que todos tienen portátil).

**¿Cuándo usarlo?**
- **Úsalo sélo** en tareas complejas de diseño (proyectos, rúbricas completas) donde el contexto es determinante.
- **Evítalo** en consultas rápidas o directas; en esos casos solo añade fricción innecesaria.

### 5) Gestión de la incertidumbre (Supuestos explícitos)

Si el modelo no tiene toda la información, tenderá a rellenar los huecos (alucinar) o a ser vago.
- **En la plantilla:** "Si falta información crítica, propón hasta 3 supuestos explícitos".
- **Por qué funciona:** Hace visible la "imaginación" del modelo. Te permite corregir la premisa ("No, no tienen portátiles, tienen tablets") antes de que genere todo el contenido.

### 6) Control del formato (para que sea usable)

Especifica el formato como si fuese una “plantilla de entrega”. Ejemplos útiles:

- Tabla de comparación con columnas fijas.
- Lista de verificación (checklist).
- Markdown con encabezados exactos.
- Las cabeceras deben tener solo la primera palabra en mayúsculas (norma RAE), salvo nombres propios.

### 7) Delimitadores (para separar instrucciones de datos)

Si incluyes textos largos (temario, contexto, instrucciones del centro), sepáralos con delimitadores para que el modelo no confunda las instrucciones del prompt con el texto a analizar:

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

## Razonamiento y verificación

En educación, muchas tareas no tienen una única respuesta “correcta” (p. ej. diseñar una actividad, redactar una rúbrica o elegir ejemplos). En esos casos funciona mejor pedir **alternativas + criterios + selección** que pedir “la mejor respuesta” a secas.

### Tree of Thoughts (ToT): explorar alternativas y elegir con criterios

Pide 2–4 propuestas distintas (A/B/C) y una evaluación con una rúbrica breve. Después, solicita **solo la versión final** integrando mejoras.

Ver ejemplo: [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

### Self-consistency: consenso (especialmente para checklists)

Pide varias propuestas independientes y luego una versión por “consenso”: conservar lo común y justificar excepciones. Es muy útil para **checklists** y pautas de corrección.

Ver ejemplo: [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

### ReAct (Reasoning + Acting): investigar y verificar con acciones observables

Cuando la tarea requiere herramientas (búsqueda, extracción, validación de formato), usa un ciclo breve de **Acción → Observación → Ajuste**. Importante: pide **acciones y evidencias**, no “pensamiento paso a paso”.

Ver ejemplo: [/docs/ejemplos/agentes-y-orquestacion](/docs/ejemplos/agentes-y-orquestacion)

### Iteración controlada (Self-Refine / Reflexion): borrador → crítica → versión final

Lo que a veces se llama “RSIP” suele corresponder a patrones más estándar como **Self-Refine** (mejora iterativa con auto-feedback) y **Reflexion** (agentes que mejoran con feedback y memoria). En docencia, basta con 1–2 rondas y **criterios de parada** claros.

Ver ejemplo: [/docs/ejemplos/agentes-y-orquestacion](/docs/ejemplos/agentes-y-orquestacion)

### Descomposición con restricciones (task decomposition / prompt chaining)

Lo que a veces se etiqueta como “CAD” suele corresponder a **descomponer** el trabajo manteniendo restricciones globales (nivel, tiempo, privacidad, formato). Pide un “blueprint” primero y el contenido después, seguido de una revisión de coherencia.

Ver ejemplo: [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

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

Si el modelo debe usar herramientas o hacer iteraciones, pide que registre **acciones y observaciones** (qué hizo y qué obtuvo) y limita el número de ciclos. Evita pedir cadenas de pensamiento explícitas.

## Guías oficiales recomendadas

- OpenAI: https://platform.openai.com/docs/guides/prompt-engineering
- Google Gemini: https://ai.google.dev/gemini-api/docs/prompting-intro


