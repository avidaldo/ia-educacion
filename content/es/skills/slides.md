---
derived_from:
  es/skills/index.md: "f28eecf86c888bb077a33a0a55fb4e7a88c89961"
---

<!-- .slide: id="no-repitas" class="statement" -->
## Si la tarea se repite, no repitas el *prompt*

Guarda las instrucciones, los materiales y el procedimiento.

---

<!-- .slide: id="tres-niveles" class="cards fragments" -->
## Tres niveles

### Instrucciones personalizadas
Se aplican a **todas** tus conversaciones.

### Asistente personalizado
Instrucciones y documentos para **las conversaciones de ese asistente**: GPT, Gem, proyecto, espacio.

### *Skill*
Un **procedimiento** que se carga solo cuando la tarea lo requiere, en cualquier conversación.

---

<!-- .slide: id="asistentes" class="table" -->
## Asistentes personalizados

| Herramienta | Nombre |
| --- | --- |
| ChatGPT | GPTs y proyectos |
| Gemini | Gems (pasan a ser *skills* desde noviembre de 2026) |
| Claude | Proyectos |
| Perplexity | Espacios |

Un *prompt* fijo más un contexto opcional, reutilizado en muchas conversaciones.

---

<!-- .slide: id="como-funciona-skill" class="fragments" -->
## Cómo funciona una *skill*

- Una carpeta con un fichero `SKILL.md`: nombre, **cuándo** usarla y **cómo** hacer la tarea.
- Puede llevar ejemplos, plantillas y código.
- El asistente solo lee al principio el nombre y la descripción.
- Cuando tu petición encaja, carga la *skill* completa y sigue el procedimiento.

Notas:
Por eso puede tener muchas skills disponibles sin llenar la conversación, y no hace falta elegir el asistente adecuado: basta con pedir la tarea. Es un estándar abierto (Agent Skills) publicado por Anthropic.

---

<!-- .slide: id="donde" class="table" -->
## Dónde se pueden usar

| Dónde | Disponibilidad |
| --- | --- |
| Claude | Todos los planes, con la ejecución de código activada |
| ChatGPT | Planes Business, Enterprise y Edu |
| Gemini | Desde octubre de 2026, cuentas personales de adultos |
| Herramientas de programación con agentes | Desde carpetas del proyecto |

---

<!-- .slide: id="ejemplo-skill" class="prompt dense" -->
## Una *skill* para preguntas de Moodle

```markdown
---
name: preguntas-gift
description: Genera preguntas de opción múltiple en formato GIFT importable en Moodle.
  Úsala cuando pidan preguntas de test, un banco de preguntas o un examen para Moodle.
---
1. Si no se indica, pregunta el nivel y el número de preguntas.
2. 4 opciones, una correcta; las incorrectas restan un 25 %.
3. Sigue exactamente el formato de ejemplo.gift.
4. Escapa ~ = # { } : en el texto.
5. Revisa la clave antes de entregar.
```

Notas:
La descripción es lo más importante: es lo que el asistente lee para decidir si la usa. La carpeta se completa con una pregunta exportada de tu propio Moodle. La versión completa está en la página.

---

<!-- .slide: id="demo-crear-skill" class="demo" -->
## Una *skill* que crea *skills*

Describir la tarea y dejar que el asistente escriba el procedimiento.

Notas:
**Demo (8 min)**. Claude (plan gratuito, con la ejecución de código activada en Ajustes → Capacidades) o ChatGPT Edu.

1. Pedir: «Quiero una *skill* que genere preguntas GIFT para Moodle con estas reglas…» y pegar las reglas de la página.
2. Revisar la descripción y las instrucciones que propone; corregir lo que no encaje.
3. Instalarla y, en un chat nuevo, pedir «diez preguntas de test sobre…» sin mencionar la *skill*.
4. Comprobar que la ha usado y revisar las preguntas.

**Resultado esperado:** el asistente reconoce la tarea y aplica el procedimiento sin que se lo recuerdes.
**Si falla:** enseñar la *skill* de ejemplo de la página.
**Mensaje clave:** es *metaprompting* aplicado a un procedimiento; la *skill* se prueba con casos reales antes de confiar en ella.

---

<!-- .slide: id="error-comun" class="comparison" -->
## Instrucciones, no descripciones

### Mal
«Crea un generador de preguntas de test que…»

### Mejor
«Cuando el usuario te dé un tema, genera 10 preguntas en formato GIFT…»

---

<!-- .slide: id="ideas" -->
## Ideas para la docencia

- Banco de preguntas con el formato de tu Moodle.
- Adaptador de materiales a varios niveles.
- Revisor de actividades con tus criterios.
- Redactor con el estilo del departamento.
- Corrector con rúbrica, sin datos identificativos.

---

<!-- .slide: id="terceros" class="statement" -->
## Instala solo *skills* que hayas leído

Como una extensión del navegador, una *skill* de terceros puede contener instrucciones o código dañinos.

---

<!-- .slide: id="antes-de-compartir" class="checklist" -->
## Antes de usarlo o compartirlo

- [ ] Objetivo y formato definidos.
- [ ] Criterios de calidad explícitos.
- [ ] Probado con casos reales, alguno difícil.
- [ ] No pide ni guarda datos del alumnado.
- [ ] Los documentos que lleva se pueden compartir.

---

<!-- .slide: id="practica-asistente" class="practice" -->
## Crea tu asistente

1. Elige una tarea que repites cada semana.
2. Escribe sus instrucciones con la plantilla de la página.
3. Crea una Gem, un GPT o un proyecto con ellas.
4. Pruébalo con dos casos reales y corrige las instrucciones.

**15 minutos.** Producto: un asistente que ya funciona.

Notas:
La plantilla está en la página, en «Cómo escribir las instrucciones». Poner en común qué tareas han elegido: suelen salir bancos de preguntas, adaptaciones y comunicaciones a familias.
