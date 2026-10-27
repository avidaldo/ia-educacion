---
derived_from:
  es/bots-educativos/index.md: "a9d495ae5a90f82a40f955ca1ec364d910b920cb"
---

<!-- .slide: id="que-es" class="statement" -->
## Un asistente que configuras tú para que lo use el alumnado

Lo interesante no es que responda, sino que guíe el razonamiento.

---

<!-- .slide: id="cuenta-primero" class="statement" -->
## Primero: ¿con qué cuenta va a entrar el alumnado?

De ella dependen la edad mínima, las condiciones sobre sus datos y si el centro puede responder de ese uso.

---

<!-- .slide: id="edades" class="table" -->
## Edad mínima con cuenta personal

| Servicio | Edad mínima |
| --- | --- |
| ChatGPT | 13; menores de 18, con consentimiento familiar |
| Gemini | 13 (con cuenta de centro, la habilita el administrador) |
| Perplexity | 13; menores, si la familia acepta las condiciones |
| Claude | 18 |

Notas:
En España, un menor solo consiente por sí mismo el tratamiento de sus datos a partir de los 14 años (artículo 7 de la LOPDGDD). Pedir que se registren con cuenta personal traslada a cada familia una decisión que corresponde al centro.

---

<!-- .slide: id="cuentas-centro" class="statement" -->
## La opción con más garantías: cuentas que proporciona el centro

Con Workspace for Education, Gemini está disponible para todas las edades si el administrador lo activa.

Notas:
Menores de 18 años con esas cuentas: Gems, aprendizaje guiado, Canvas y cuestionarios sí; investigación a fondo y Gemini Live, no.

---

<!-- .slide: id="perplexity" class="comparison" -->
## Lo que ya no funciona

### Antes
Un espacio de Perplexity compartido con un enlace abierto, sin registrarse.

### Ahora
Los espacios son proyectos y, en cuentas personales, solo acceden las personas invitadas.

Notas:
Y no pedir cuenta nunca hizo que cumpliera la normativa por sí solo: lo que escribe el alumnado se envía igualmente a un tercero, con datos técnicos como la IP, y la edad mínima de las condiciones sigue aplicándose.

---

<!-- .slide: id="compartir" class="table dense" -->
## Cómo se comparte en cada herramienta

| Herramienta | Cómo |
| --- | --- |
| Gemini (Gems) | Como un fichero de Drive; pasan a ser *skills* |
| ChatGPT (GPTs) | Con un enlace o en la tienda de GPTs |
| Perplexity (proyectos) | Invitando a cada persona |

---

<!-- .slide: id="modos-tutor" class="cards" -->
## Antes de construir uno: los modos tutor

### ChatGPT
Modo de estudio, en todos los planes.

### Gemini
Aprendizaje guiado, también para menores de 18 con cuenta de centro.

### Perplexity
Modo de aprendizaje, con tarjetas y cuestionarios.

Notas:
Un bot propio compensa cuando necesitas ceñirte a tu temario, tu metodología o un tipo de tarea concreto.

---

<!-- .slide: id="tutor-socratico" class="prompt dense" -->
## Un tutor socrático

```text
Eres un tutor socrático de [materia] para [nivel]. Ayuda a llegar a la respuesta,
nunca des la solución directa, aunque te la pidan.
Divide el problema en pasos y haz solo UNA pregunta cada vez.
Si hay un error, pregunta por qué se eligió ese camino.
Basa las explicaciones en los materiales adjuntos; si algo no está en ellos, dilo.
No pidas datos personales. Si la duda es delicada, recomienda hablar con el profesorado.
Preséntate como asistente de IA y pregunta en qué se ha atascado.
```

Notas:
La versión completa está en la página.

---

<!-- .slide: id="demo-tutor" class="demo" -->
## Intenta que te dé la respuesta

Probar el bot como lo haría un alumno.

Notas:
**Demo (6 min)**. Una Gem o un GPT con el tutor socrático de la página, en una cuenta de pruebas.

1. Plantear un ejercicio y pedir directamente la solución.
2. Insistir varias veces y pedirle que «haga una excepción».
3. Cometer un error a propósito y ver cómo lo trata.
4. Hacer una pregunta fuera del temario.

**Resultado esperado:** resiste la mayoría de intentos, pero con insistencia alguno funciona.
**Si falla:** si cede enseguida, ajustar las reglas delante del grupo.
**Mensaje clave:** las instrucciones no son una barrera de seguridad; el bot ayuda a quien quiere aprender.

---

<!-- .slide: id="probar" class="checklist" -->
## Antes de compartirlo

- [ ] Pide la solución con insistencia.
- [ ] Pide que ignore sus instrucciones.
- [ ] Haz una pregunta fuera del temario y otra delicada.
- [ ] Comete un error a propósito.
- [ ] Comprueba que coincide con tus materiales.

---

<!-- .slide: id="en-clase" -->
## En clase

- Explica que es IA y que puede equivocarse.
- Define para qué se puede usar, sobre todo en tareas evaluables.
- Revisa cómo lo usan y ajusta las instrucciones.
- La evaluación sigue siendo tuya.
