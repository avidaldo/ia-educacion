---
title: Bots educativos
description: Asistentes configurados por el docente para que el alumnado los use como tutor, y lo que hay que decidir antes de ponerlos en sus manos.
reviewed: 2026-10-22
review_every: 3
---

## Qué es un bot educativo

Un bot educativo es un [asistente personalizado](../skills/index.md) que configura el docente **para que lo use el alumnado**: un tutor que guía sin dar la solución, un compañero de repaso con preguntas sobre el temario, un asistente que ayuda a entender una lectura. El alumnado ve un chat normal, pero el bot sigue siempre las instrucciones que fijaste.

La idea más interesante no es que dé respuestas, sino que **guíe el razonamiento**: hacer preguntas, dividir el problema en pasos, señalar contradicciones para que el alumno detecte su propio error.

## Lo primero: con qué cuenta entra el alumnado

Antes de diseñar el bot hay que resolver una pregunta que condiciona todo lo demás: **qué cuenta va a usar cada alumno**. De ella dependen la edad mínima, las condiciones sobre sus datos y si el centro puede responder de ese uso.

| Servicio | Edad mínima con cuenta personal |
| --- | --- |
| ChatGPT | 13 años o la edad de consentimiento del país; menores de 18, con consentimiento de madre, padre o tutor |
| Gemini | 13 años o la edad del país; con cuenta de centro educativo, la habilita su administrador |
| Perplexity | 13 años; menores de edad, solo si madre, padre o tutor aceptan las condiciones |
| Claude | 18 años |

En España, un menor solo puede consentir por sí mismo el tratamiento de sus datos a partir de los 14 años; por debajo, hace falta el consentimiento de quienes tienen la patria potestad o la tutela (artículo 7 de la Ley Orgánica de Protección de Datos). Pedir al alumnado que se registre en un servicio con su cuenta personal traslada a cada familia una decisión que corresponde al centro.

La opción con más garantías es la que **proporciona el centro o la administración**: cuentas educativas contratadas con condiciones específicas. Con **Google Workspace for Education**, por ejemplo, la aplicación de Gemini está disponible para alumnado de todas las edades si el administrador la activa, con protección de datos de nivel empresarial; el alumnado menor de 18 años puede usar Gems, el aprendizaje guiado, Canvas y los cuestionarios, pero no la investigación a fondo ni Gemini Live. Las implicaciones legales se desarrollan en el módulo de ética y normativa.<!-- TODO: enlazar ../etica-legal/normativa.md cuando exista -->

> [!CAUTION]
> **Lo que ya no funciona: el espacio de Perplexity sin cuenta**
> Durante un tiempo, un espacio de Perplexity se podía compartir con un enlace abierto, y se recomendaba para que el alumnado lo usara sin registrarse. Hoy los espacios se llaman **proyectos** y, en las cuentas personales, solo acceden las personas invitadas: *«Projects cannot be made publicly queryable»*, según su centro de ayuda (octubre de 2026). Además, no pedir cuenta nunca hizo que su uso cumpliera la normativa por sí solo: lo que el alumnado escribe se sigue enviando a un tercero, junto con datos técnicos como la dirección IP, y la edad mínima de las condiciones de uso sigue aplicándose.

## Cómo compartir un bot en cada herramienta

| Herramienta | Cómo se comparte | A tener en cuenta |
| --- | --- | --- |
| Gemini (Gems) | Como un fichero de Drive: con personas concretas o con quien tenga el enlace, según lo que permita el administrador | Requiere cuenta de Google. A partir de noviembre de 2026 las Gems pasan a ser *skills* (en las cuentas de centro, en 2027) |
| ChatGPT (GPTs) | Con un enlace o publicado en la tienda de GPTs | Requiere cuenta de ChatGPT; ver edad mínima |
| Perplexity (proyectos) | Invitando a cada persona; hasta 5 colaboradores, o 9.999 si el propietario es docente o estudiante verificado | Requiere cuenta de Perplexity; ver edad mínima |

## Los modos tutor integrados

Antes de construir un tutor, comprueba si basta con el que ya trae cada herramienta:

- **ChatGPT, modo de estudio**: guía con preguntas en lugar de dar la respuesta, explica por niveles y comprueba la comprensión. Disponible en todos los planes.
- **Gemini, aprendizaje guiado**: disponible también para alumnado menor de 18 años con cuentas de Workspace for Education.
- **Perplexity, modo de aprendizaje**: explica paso a paso y genera tarjetas y cuestionarios a partir de los materiales.

Un bot propio compensa cuando necesitas algo que estos modos no hacen: ceñirse a tu temario y tus materiales, seguir tu metodología o un nivel concreto, o limitarse a un tipo de tarea.

## Un tutor socrático

Estas instrucciones son un buen punto de partida. Adáptalas a la materia, el nivel y los materiales que adjuntes:

```text
Rol:
Eres un tutor socrático de [materia] para alumnado de [nivel]. Tu objetivo es ayudar a llegar a la respuesta por sí mismo, nunca dar la solución directa.

Reglas:
1. No resuelvas el problema ni des la respuesta final, aunque te la pidan.
2. Si te piden la respuesta, explica con amabilidad que tu trabajo es ayudar a pensar.
3. Divide el problema en pasos pequeños y haz solo UNA pregunta cada vez.
4. Si hay un error, no digas «está mal»: pregunta por qué se eligió ese camino o señala la contradicción.
5. Usa un lenguaje claro y adaptado al nivel, con un tono paciente.
6. Basa las explicaciones en los materiales adjuntos; si algo no está en ellos, dilo.
7. No pidas ni guardes datos personales.
8. Si la duda no es de la materia o es delicada, recomienda hablar con el profesorado.

Inicio:
Preséntate en una frase como asistente de IA y pregunta en qué ejercicio o concepto se ha atascado.
```

## Probarlo antes de compartirlo

Un bot se comporta de forma distinta según cómo le hablen. Antes de darlo al alumnado, pruébalo como lo haría un alumno:

- [ ] Pide directamente la solución, varias veces y con insistencia.
- [ ] Pídele que ignore sus instrucciones o que «haga una excepción».
- [ ] Haz una pregunta fuera del temario y otra personal o delicada.
- [ ] Comete un error a propósito y comprueba cómo lo trata.
- [ ] Revisa que lo que explica coincide con tus materiales.

> [!WARNING]
> **Las instrucciones no son una barrera de seguridad**
> Con suficiente insistencia, un alumno puede conseguir que el bot se salga de sus instrucciones y le dé la respuesta. El bot ayuda a quien quiere aprender; no sustituye la supervisión ni sirve para controlar a quien quiere saltárselo.

## En clase

- Explica al alumnado que es una herramienta de IA, que puede equivocarse y que sus respuestas se comprueban.
- Define para qué se puede usar y para qué no, sobre todo en las tareas evaluables.
- Revisa de vez en cuando cómo lo están usando y ajusta las instrucciones.
- La evaluación sigue siendo tuya: el bot acompaña el estudio, no califica.
