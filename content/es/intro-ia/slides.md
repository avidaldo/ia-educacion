---
derived_from:
  es/intro-ia/index.md: "092b9369e10fe8c4f69fb793a24a4bab55e19b09"
  es/intro-ia/funcionamiento.md: "85900217673a2a2f9c7585cce76fe1c774c77bc3"
---

<!-- .slide: id="setenta-anos" class="statement" -->
## «La IA» es la parte más reciente de un campo con setenta años

Inteligencia artificial, aprendizaje automático, aprendizaje profundo e IA generativa no son sinónimos.

---

<!-- .slide: id="conjuntos" class="image-full" -->
![Diagrama de cuatro conjuntos anidados: la inteligencia artificial contiene el aprendizaje automático, que contiene el aprendizaje profundo, que contiene la IA generativa](../../assets/intro-ia/ia-aprendizaje-generativa.svg)

Notas:
ELIZA (1966) y Deep Blue (1997) eran IA sin aprendizaje: reglas escritas a mano y mucho cálculo. El aprendizaje profundo despega en 2012 y la IA generativa se populariza a finales de 2022.

---

<!-- .slide: id="reglas-o-datos" class="image-full" -->
![Esquema: en la programación clásica, reglas y datos entran en un programa que produce respuestas; en el aprendizaje automático, datos y respuestas entran en un entrenamiento que produce un modelo](../../assets/intro-ia/programacion-y-aprendizaje.svg)

Notas:
El cambio de planteamiento: en lugar de escribir las reglas, se le dan al programa datos con sus respuestas y el entrenamiento extrae las reglas. El resultado es un modelo. Ejemplos cotidianos anteriores a los chatbots: filtros de spam, recomendaciones, predicción del tiempo.

---

<!-- .slide: id="moravec" class="statement" -->
## Lo difícil para nosotros es fácil para un ordenador, y al revés

La paradoja de Moravec: la IA redacta un informe impecable y falla en una pregunta de sentido común.

---

<!-- .slide: id="por-que-ahora" class="cards fragments" -->
## Por qué ahora

### Cálculo
GPU y chips específicos para entrenar redes enormes.

### Datos
La web, libros digitalizados y código público.

### Arquitecturas
El *transformer* (2017) escala los modelos de lenguaje.

### Inversión
Desde 2022, recursos sin precedentes.

---

<!-- .slide: id="linea-temporal" class="timeline" -->
## Una línea temporal

- **2012** AlexNet inicia el auge del aprendizaje profundo.
- **2017** Se publica la arquitectura *transformer*.
- **2020** GPT-3 hace tareas para las que no se entrenó.
- **2022** ChatGPT populariza los asistentes conversacionales.
- **2024** Modelos que razonan antes de responder.
- **2025** Pesos abiertos baratos, vídeo con sonido, navegadores con agentes.

---

<!-- .slide: id="modelo-chatbot-agente" class="cards" -->
## Tres cosas distintas

### Modelo
El sistema entrenado que genera texto. GPT-5, Gemini, Claude Sonnet.

### *Chatbot*
El producto con el que conversamos: modelo más interfaz, memoria, búsqueda, ficheros.

### Agente
Recibe un objetivo y **actúa**: planifica, usa herramientas y decide el siguiente paso.

Notas:
A un chatbot le preguntas y te responde; a un agente le encargas una tarea y la ejecuta, con los riesgos que eso implica.

---

<!-- .slide: id="como-funciona" class="section" -->
## Cómo funciona un modelo de lenguaje

---

<!-- .slide: id="siguiente-palabra" class="statement" -->
## Predice la siguiente palabra, una y otra vez

Como el teclado del móvil, pero entrenado con una cantidad enorme de texto y teniendo en cuenta todo lo anterior.

---

<!-- .slide: id="plausible" class="statement" -->
## Genera lo más plausible; no comprueba lo que dice

Casi siempre coincide con lo correcto. Cuando no, el error suena igual de seguro.

---

<!-- .slide: id="tokens-contexto" class="two-col" -->
## *Tokens* y ventana de contexto

### *Tokens*
Fragmentos de texto con los que trabaja el modelo. En español, una palabra ocupa a menudo más de uno.

### Ventana de contexto
Lo que el modelo tiene en cuenta a la vez: instrucciones, conversación, adjuntos y respuesta. Lo que queda fuera no existe para él.

---

<!-- .slide: id="base-asistente" class="two-col" -->
## Del modelo base al asistente

### Preentrenamiento
Aprende a predecir el siguiente *token* sobre enormes cantidades de texto. Sabe continuar textos, no seguir instrucciones.

### Ajuste posterior
Con conversaciones de ejemplo y valoraciones humanas aprende a comportarse como asistente: seguir instrucciones, dar formato, negarse.

Notas:
El tono servicial y la tendencia a dar la razón no son una personalidad: son comportamientos aprendidos en esta fase.

---

<!-- .slide: id="demo-respuestas-distintas" class="demo" -->
## La misma pregunta, dos respuestas

El modelo elige entre las palabras más probables con un componente de azar.

Notas:
**Demo (3 min)**. Cualquier *chatbot*, en dos chats temporales.

1. Hacer la misma petición abierta en los dos chats (por ejemplo, «Propón una actividad de 20 minutos para introducir la fotosíntesis en 2.º de ESO»).
2. Poner las dos respuestas lado a lado.
3. Regenerar una de ellas y mostrar que vuelve a cambiar.

**Resultado esperado:** propuestas distintas, igual de seguras.
**Si falla:** explicar con la página que cada palabra se elige entre una distribución de probabilidades.
**Mensaje clave:** cuando el resultado importa, regenera o compara.

---

<!-- .slide: id="alucinaciones" -->
## Alucinaciones

- Respuesta fluida y segura que es **falsa**: datos, citas, referencias inventadas.
- No es un fallo puntual: el entrenamiento premia más arriesgar una respuesta que decir «no lo sé».
- Los modelos actuales fallan menos, sobre todo con la búsqueda web, pero el riesgo no desaparece.
- **Toda cifra, cita, referencia o norma se comprueba en la fuente.**

---

<!-- .slide: id="demo-referencias" class="demo" -->
## ¿Existen estas referencias?

Pedir bibliografía y comprobarla.

Notas:
**Demo (5 min)**. Cualquier *chatbot*, en un chat temporal y sin búsqueda web si se puede desactivar.

1. Pedir tres referencias académicas sobre un tema muy concreto de tu materia.
2. Buscar cada título en un buscador académico.
3. Repetir la petición con la búsqueda web activada y abrir las fuentes que cita.

**Resultado esperado:** alguna referencia verosímil que no existe o con datos cambiados; con búsqueda, fuentes reales que hay que leer igualmente.
**Si falla:** si todas existen, comprobar que los datos (autores, año, revista) coinciden.
**Mensaje clave:** plausible no es verdadero; lo que vaya a un documento se comprueba en la fuente.

---

<!-- .slide: id="sabe-busca" class="two-col" -->
## Lo que sabe y lo que busca

### Fecha de corte
Lo que pasó después del entrenamiento no está en el modelo.

### Búsqueda web
Los *chatbots* buscan y citan páginas. Mejora la actualidad, pero puede elegir mal las fuentes o resumirlas mal.

Notas:
Matiz: el modelo puede reproducir de forma literal fragmentos de sus datos de entrenamiento, sobre todo textos muy repetidos. De ahí parte de los conflictos sobre derechos de autor y la recomendación de no introducir datos personales.

---

<!-- .slide: id="razonan" -->
## Modelos que razonan

- Generan un razonamiento intermedio antes de responder.
- Mejoran mucho en matemáticas, programación y lógica, a cambio de tiempo.
- Siguen siendo texto generado: no son deducción infalible.
- El razonamiento que muestran no siempre refleja lo que determinó la respuesta.

---

<!-- .slide: id="sesgos" class="statement" -->
## Los sesgos son un reflejo de los datos

No una «decisión» del modelo, y corregirlos introduce otros desequilibrios.
