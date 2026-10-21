---
title: Diseño de prompts
description: Cómo especificar una tarea para que el resultado sea un material útil y verificable, no una respuesta genérica.
reviewed: 2026-04-30
---

## Qué es un buen *prompt*

Un *prompt* eficaz funciona como una **especificación**: dice qué producto quieres, para quién, con qué restricciones y cómo sabrás que está bien. Cuanto más se parece a un encargo bien redactado a una persona competente, mejor funciona.

En docencia conviene orientarlo a **materiales funcionales y verificables**, por ejemplo:

- fichas de actividad con la secuencia y los tiempos;
- bancos de preguntas en formatos que Moodle importa directamente (GIFT, XML);
- rúbricas con indicadores observables;
- adaptaciones que mantengan la alineación con los objetivos de aprendizaje.

## Una estructura de referencia

Esta plantilla sirve de punto de partida. No hace falta rellenar todos los apartados en cada consulta: es una lista de lo que más influye en el resultado.

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

## Las técnicas que más se notan

### Definir un rol

Asignar un rol no hace al modelo «más listo»: **comprime instrucciones**. Un rol desplaza la respuesta hacia el vocabulario, el tono y los criterios asociados a esa figura en los textos con los que se entrenó el modelo. Sirve sobre todo para fijar el **estilo** de la respuesta, y deja de ser necesario cuando la descripción del resultado ya es suficientemente detallada.

Mal uso
: «Eres un experto en Python.» Delegas en el modelo qué significa «experto», y puede tirar de prácticas que no quieres (por ejemplo, librerías obsoletas).

Buen uso
: «Actúa como auditor de seguridad: revisa este código buscando vulnerabilidades críticas (OWASP Top 10) y sugiere correcciones.» El rol fija la perspectiva; las instrucciones definen la tarea.

El rol configura el *quién* (la voz), pero no sustituye al *qué* (las instrucciones). Si para una tarea factual confías solo en el rol, aumentas el riesgo de respuestas plausibles pero falsas.

### Un objetivo claro, con su evidencia

Mal: «Haz una actividad sobre IA.»

Mejor: «Crea una actividad de 50 minutos para 2.º de FP sobre cómo **evaluar respuestas de una IA**. Evidencia: el alumnado identifica 3 errores típicos y propone 1 mejora.»

### El contexto docente mínimo

Incluye siempre **nivel**, **tiempo**, **recursos** y **producto final**. Con esos cuatro datos desaparece la mayoría de las respuestas genéricas.

### Pedir que te pregunte primero

Consiste en pedir al modelo que te entreviste antes de generar la respuesta («Hazme 3–5 preguntas de aclaración, solo las necesarias»). Le obliga a detectar huecos en tu petición antes de rellenarlos por su cuenta, por ejemplo suponiendo que todo el grupo tiene portátil.

- **Úsalo** en tareas de diseño complejas (proyectos, rúbricas completas), donde el contexto lo decide todo.
- **Evítalo** en consultas rápidas: solo añade un paso.

### Supuestos explícitos

Si al modelo le falta información, tenderá a rellenar los huecos o a ser vago. Pedirle «si falta información crítica, propón hasta 3 supuestos explícitos» hace visible lo que está suponiendo, y te permite corregirlo («no tienen portátiles, tienen tabletas») antes de que construya todo encima.

### El formato de entrega

Especifica el formato como si fuera una plantilla de entrega:

- una tabla de comparación con columnas fijas;
- una lista de verificación;
- Markdown con encabezados exactos;
- títulos con mayúscula solo en la primera palabra (norma RAE), salvo nombres propios.

### Delimitadores

Si incluyes textos largos (temario, normas del centro, un texto del alumnado ya anonimizado), sepáralos con delimitadores para que el modelo no confunda tus instrucciones con el texto que debe analizar. Sirven las comillas triples o etiquetas con nombre, como `<temario>…</temario>`; lo importante es usar siempre las mismas y nombrarlas en la instrucción:

```text
Contexto del centro:
"""
[pega aquí el texto]
"""
```

## Revisar antes de dar por buena una respuesta

### Dos pasadas: borrador, auditoría y versión final

Pide primero una versión y después una auditoría contra criterios:

```text
Revisa tu propuesta con esta lista:
1) ¿El objetivo es observable?
2) ¿Hay riesgos de privacidad?
3) ¿La evaluación mide lo que se pretende?
4) ¿Hay supuestos no declarados?

Devuelve: (a) hallazgos, (b) versión mejorada.
```

### Comparar dos versiones

En lugar de «mejóralo», da dos versiones y pide una tabla por criterios:

```text
Compara el prompt A con el B por: claridad, formato, verificabilidad y riesgos.
Devuelve una tabla y una recomendación.
```

### No inventar

En docencia el problema no es solo acertar: es **no inventar**. Incluye restricciones como:

- «Si necesitas datos (fechas, normativa, estadísticas), indícalo y sugiere cómo verificarlos. No inventes.»
- «Marca claramente lo que sea un supuesto.»

> [!WARNING]
> **Estas instrucciones reducen el problema, no lo eliminan**
> Un modelo de lenguaje no sabe cuándo no sabe: puede presentar un dato inventado con la misma seguridad que uno correcto. Las cifras, las citas y la normativa se comprueban siempre en la fuente.

## *Metaprompting*: pedirle a la IA que escriba el *prompt*

Cuando una tarea se repite (generar tests, adaptar actividades, redactar rúbricas), compensa pedir primero **el *prompt* reutilizable** en lugar del resultado. Describes qué debe hacer ese *prompt*, qué debe preguntar y qué formato debe exigir, y el modelo te devuelve una plantilla que puedes revisar, guardar y reutilizar o convertir en un asistente personalizado.

Funciona por dos motivos: te obliga a pensar los requisitos antes de pedir el producto, y el modelo suele redactar instrucciones más completas de lo que escribiríamos a mano. El riesgo es el mismo de siempre: la plantilla hay que leerla y probarla antes de confiar en ella.

Hay un ejemplo completo en [Ejemplos comentados](ejemplos.md#un-prompt-que-escribe-prompts).

## Modelos que razonan

Los modelos actuales pueden dedicar tiempo a «pensar» antes de responder. Con ellos suele funcionar mejor:

- pedir una respuesta **directa**;
- pedir **supuestos** si falta información;
- y pedir una **justificación breve** basada en criterios, no un razonamiento largo.

No hace falta pedirles que piensen «paso a paso»: ya lo hacen. Si la salida está bien especificada, el modelo se organiza solo.

## Dar ejemplos de salida

Los ejemplos sirven sobre todo para **estilo y formato**, no para enseñar contenido.

*Zero-shot*
: Solo la instrucción, sin ejemplos.

*One-shot*
: Un ejemplo de la salida deseada.

*Few-shot*
: Dos o tres ejemplos, cuando el formato es complejo o delicado (por ejemplo, rúbricas o preguntas para Moodle).

## Cuando el chat no basta

Un **agente** tiene sentido cuando quieres que el sistema siga un plan, use herramientas (convertir a GIFT, aplicar una rúbrica, revisar un formato) y pare cuando se cumplan unos criterios. Si diseñas un flujo así, especifica:

- el objetivo y los criterios de parada;
- las herramientas permitidas;
- las restricciones (privacidad, fuentes);
- el formato de salida.

Las técnicas para tareas largas o con varias alternativas están en [Técnicas avanzadas](avanzado.md).

## Guías oficiales

- [OpenAI: *prompt engineering*](https://platform.openai.com/docs/guides/prompt-engineering)
- [Google: estrategias de *prompting* para Gemini](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [Anthropic: *prompt engineering* para Claude](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- Para quien quiera la visión de conjunto académica: Schulhoff et al. (2024), [*The Prompt Report*](https://arxiv.org/abs/2406.06608), una revisión sistemática de 58 técnicas de *prompting* de texto.
