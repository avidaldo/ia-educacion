---
---

<!-- .slide: id="especificacion" class="statement" -->
## Un buen *prompt* es una especificación

Dice qué producto quieres, para quién, con qué restricciones y cómo sabrás que está bien.

Notas:
**Mensaje clave:** pedirle algo a una IA se parece más a encargar un trabajo a una persona competente que a buscar en Google. Lo que no se especifica, el modelo lo rellena por su cuenta.

---

<!-- .slide: id="ingredientes" class="cards fragments" -->
## Lo que más influye en el resultado

### Tarea
Qué producto quieres: actividad, rúbrica, banco de preguntas…

### Contexto
Nivel, tiempo, recursos y perfil del grupo, sin datos personales.

### Salida
Formato, encabezados fijos y límites de extensión.

### Restricciones
No inventar normativa ni cifras; marcar los supuestos.

Notas:
Estas cuatro piezas son la plantilla de la página. No hace falta usarlas todas en cada consulta: son una lista de comprobación.

---

<!-- .slide: id="plantilla" class="prompt dense" -->
## Una plantilla de partida

```text
Eres un consultor experto en diseño curricular.
Tarea: quiero crear [actividad / banco de preguntas / rúbrica].
Contexto: materia, nivel, duración, recursos, perfil del grupo (sin datos personales).
Antes de responder: hazme 3–5 preguntas de aclaración; si falta información, propón hasta 3 supuestos explícitos.
Salida: Markdown, con estos encabezados: […]; máx. 1 página.
Restricciones: no inventes normativa, datos ni cifras; si no lo sabes, dilo.
```

Notas:
La versión completa está en la página, con todos los apartados. Copiarla desde la web, no desde la diapositiva.

---

<!-- .slide: id="rol" class="comparison" -->
## El rol fija la voz, no la tarea

### Mal
«Eres un experto en Python.»

Delegas en el modelo qué significa «experto».

### Mejor
«Actúa como auditor de seguridad: revisa este código buscando vulnerabilidades críticas (OWASP Top 10) y sugiere correcciones.»

El rol da la perspectiva; las instrucciones, la tarea.

Notas:
Un rol desplaza la respuesta hacia el vocabulario y los criterios asociados a esa figura. No hace al modelo «más listo». Si la tarea es factual y solo damos un rol, aumentamos el riesgo de respuestas plausibles pero falsas.

---

<!-- .slide: id="objetivo" class="comparison" -->
## Un objetivo claro, con su evidencia

### Mal
«Haz una actividad sobre IA.»

### Mejor
«Crea una actividad de 50 minutos para 2.º de FP sobre cómo **evaluar respuestas de una IA**. Evidencia: el alumnado identifica 3 errores típicos y propone 1 mejora.»

Notas:
Preguntar al grupo qué le falta a la primera versión antes de enseñar la segunda. Salen solos: nivel, duración, producto final.

---

<!-- .slide: id="contexto" class="fragments" -->
## El contexto docente mínimo

- **Nivel**: curso o ciclo.
- **Tiempo**: duración de la sesión o de la tarea.
- **Recursos**: aula, proyector, móviles, internet…
- **Producto final**: qué entrega el alumnado.

Con estos cuatro datos desaparece la mayoría de las respuestas genéricas.

---

<!-- .slide: id="preguntar-primero" class="two-col" -->
## Pedir que te pregunte primero

### Úsalo
En tareas de diseño complejas (proyectos, rúbricas completas), donde el contexto lo decide todo.

### Evítalo
En consultas rápidas: solo añade un paso.

Notas:
Formulación: «Hazme 3–5 preguntas de aclaración, solo las necesarias». Obliga a detectar huecos antes de rellenarlos, por ejemplo suponiendo que todo el grupo tiene portátil.

---

<!-- .slide: id="supuestos" -->
## Supuestos explícitos

- Si falta información, el modelo rellena los huecos o se vuelve vago.
- Pídele: «si falta información crítica, propón hasta 3 supuestos explícitos».
- Así ves lo que está suponiendo y lo corriges antes de que construya todo encima.

---

<!-- .slide: id="formato" class="two-col" -->
## Formato y delimitadores

### Formato de entrega
- Tabla con columnas fijas.
- Lista de verificación.
- Markdown con encabezados exactos.

### Delimitadores
Separa tus instrucciones del texto que debe analizar:

```text
Contexto del centro:
"""
[texto]
"""
```

---

<!-- .slide: id="demo-metaprompting" class="demo" -->
## Un *prompt* que escribe *prompts*

Pedir la plantilla reutilizable en lugar del resultado.

Notas:
**Demo (5 min)**. Cualquier *chatbot* (ChatGPT, Gemini o Claude), en un chat temporal.

1. Pegar el primer ejemplo de la página «Ejemplos comentados» («Actúa como un asesor pedagógico… Devuélveme SOLO el prompt final»).
2. Leer en voz alta la plantilla que devuelve: preguntas de aclaración, supuestos, encabezados fijos.
3. Abrir un chat nuevo, pegar la plantilla y rellenar el tema con una propuesta del grupo.
4. Mostrar que el modelo hace primero las preguntas de aclaración.

**Resultado esperado:** una plantilla parecida a la de la página, y una actividad que empieza preguntando.
**Si falla:** enseñar la conversación de la página.
**Mensaje clave:** para tareas que se repiten, la plantilla vale más que el resultado, y se puede convertir en un asistente personalizado.

---

<!-- .slide: id="revisar" class="checklist" -->
## Antes de dar por buena una respuesta

- [ ] Pide una **segunda pasada**: auditoría contra criterios y versión mejorada.
- [ ] Si dudas entre dos versiones, pide una **comparación en tabla** por criterios.
- [ ] Exige que marque los **supuestos** y que no invente datos.
- [ ] Comprueba **cifras, citas y normativa** en la fuente.

---

<!-- .slide: id="no-sabe" class="statement" -->
## Un modelo de lenguaje no sabe cuándo no sabe

Puede presentar un dato inventado con la misma seguridad que uno correcto.

Notas:
Las instrucciones contra la invención reducen el problema, no lo eliminan. Por eso la última casilla de la diapositiva anterior no es opcional.

---

<!-- .slide: id="razonadores" -->
## Con los modelos que razonan

- Pide una respuesta **directa**.
- Pide **supuestos** si falta información.
- Pide una **justificación breve** basada en criterios.
- No hace falta pedir que piensen «paso a paso»: ya lo hacen.

---

<!-- .slide: id="ejemplos-salida" class="table" -->
## Dar ejemplos de salida

| Técnica | Qué das | Cuándo |
| --- | --- | --- |
| *Zero-shot* | Solo la instrucción | Tareas sencillas |
| *One-shot* | Un ejemplo de la salida | Formatos concretos (una ficha, una pregunta de Moodle) |
| *Few-shot* | Dos o tres ejemplos | Formatos complejos o delicados (rúbricas) |

Notas:
Los ejemplos sirven para estilo y formato, no para enseñar contenido. Enlaza con el método de los tests de Moodle: exportar una pregunta real y dársela como ejemplo.

---

<!-- .slide: id="practica-reescribir" class="practice" -->
## Reescribe un *prompt* vago

1. Parte de: «Haz una actividad sobre IA para mis alumnos.»
2. Añade nivel, tiempo, recursos y producto final.
3. Pide preguntas de aclaración y un formato de entrega.
4. Pruébalo y pide después una crítica del propio *prompt*.

**10 minutos.** Producto: tu *prompt* y la respuesta obtenida.

Notas:
Si hay tiempo, poner en común dos o tres *prompts* y compararlos con la tabla de la página «Ejemplos comentados».
