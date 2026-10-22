---
derived_from:
  es/navegadores-agenticos/index.md: "ccdd663ba35cad5ddf4e705ef1c0e0a6418f725c"
---

<!-- .slide: id="actuar" class="statement" -->
## Un agente no solo lee la página: actúa en ella con tus sesiones abiertas

Hace clic, escribe y rellena formularios en tu nombre.

---

<!-- .slide: id="leer-o-actuar" class="comparison" -->
## Dos niveles de ayuda muy distintos

### Asistente de lectura
Resume, compara y extrae datos de las pestañas. No toca nada.

### Agente de navegación
Hace clic, escribe y pasa de una web a otra, identificado como tú en cada una.

---

<!-- .slide: id="herramientas" class="table dense" -->
## Qué hay hoy

| Herramienta | Disponibilidad |
| --- | --- |
| Comet (Perplexity) | Gratuito; Windows, Mac, iOS y Android |
| Claude en Chrome | Planes de pago; solo Chrome de escritorio |
| ChatGPT | Extensión para varios navegadores y aplicación de escritorio |
| Gemini en Chrome | No disponible en España |

Notas:
Situación en octubre de 2026. Atlas, el navegador de OpenAI, se retiró en agosto de 2026, menos de un año después de su lanzamiento: mejor no construir una forma de trabajar alrededor de una herramienta concreta.

---

<!-- .slide: id="usos" class="two-col" -->
## Compensa con webs públicas y tareas que puedes comprobar

### Sí
Comparar páginas, extraer plazos a una tabla, guiarte por una web complicada, comprobar tu propia web.

### No
Webs con datos de otras personas: XADE, las calificaciones, el correo con el alumnado y las familias.

Notas:
Lo desaconseja el propio Anthropic: lo que hay en pantalla se envía al proveedor, y un error o un ataque se ejecutaría con tus permisos.

---

<!-- .slide: id="inyeccion" class="statement" -->
## El agente no distingue tus instrucciones de las que alguien escondió en la página

Es la inyección de *prompts*.

---

<!-- .slide: id="ncsc" class="quote" -->
## No es un fallo que se arregle con una actualización

> Es muy posible que la inyección de *prompts* nunca se mitigue del todo, como sí puede hacerse con la inyección de SQL.

Centro Nacional de Ciberseguridad del Reino Unido, diciembre de 2025

Notas:
El motivo es el funcionamiento del modelo: recibe un único texto y predice cómo continuarlo, sin separar datos e instrucciones. OpenAI dice lo mismo: como las estafas en la web, «difícilmente se resolverá nunca del todo».

---

<!-- .slide: id="caso-comet" class="fragments" -->
## Bastaba con pulsar «resumir»

- Un comentario de Reddit escondía instrucciones.
- El asistente fue a la cuenta de Perplexity del usuario y copió su correo.
- Pidió un código de acceso y lo leyó en Gmail.
- Publicó ambos datos en una respuesta al comentario.

Notas:
Investigación de Brave sobre Comet, agosto de 2025. Hoy los proveedores entrenan sus modelos contra estos ataques y piden confirmación antes de las acciones delicadas; Anthropic habla de menos de un 0,08 % de ataques con éxito en sus pruebas internas, y aun así advierte de que el riesgo no es cero.

---

<!-- .slide: id="triada" class="cards" -->
## La tríada letal: el peligro está en reunir las tres

### Datos privados
Tus sesiones, tu correo, tus documentos.

### Contenido ajeno
Páginas, correos y comentarios que no controlas.

### Comunicación hacia fuera
Enviar, publicar, abrir una dirección.

Notas:
Simon Willison, junio de 2025. Un agente de navegación con tus sesiones abiertas reúne las tres; cada medida de protección quita una o la limita.

---

<!-- .slide: id="demo-inyeccion" class="demo" -->
## Una instrucción escondida en una página

¿Obedece el asistente al texto oculto?

Notas:
**Demo (5 min)**. Comet o Claude en Chrome, en un perfil de navegador sin sesiones abiertas, con la página de demostración guardada como `demo.html`.

1. Abrir `demo.html`: parece una página normal sobre el ciclo del agua.
2. Pedir al asistente «resume esta página».
3. Leer el resumen en voz alta.
4. Seleccionar todo el texto (Ctrl+A) para que aparezca la instrucción oculta.

**Resultado esperado:** el resumen termina con «Las ranas también opinan», o el asistente avisa de la instrucción.
**Si falla:** los dos resultados sirven; si no hay agente disponible, enseñar el código de la página y explicar qué haría.
**Mensaje clave:** el texto que el agente lee también puede darle órdenes.

---

<!-- .slide: id="con-cabeza" class="checklist" -->
## Cómo usarlos con cabeza

- [ ] Un perfil de navegador sin sesiones sensibles.
- [ ] Encargos concretos y acotados.
- [ ] Webs de confianza primero.
- [ ] Leer cada confirmación antes de aceptar.
- [ ] Bloquear los sitios sensibles en los ajustes.
- [ ] Detener la tarea si hace algo inesperado.

Notas:
Si manejas datos sensibles y no necesitas el agente, ChatGPT tiene un *Lockdown Mode* que limita las conexiones hacia fuera; a cambio, desactiva la navegación en directo, la investigación a fondo y el modo agente.

---

<!-- .slide: id="responsable" class="statement" -->
## Lo que hace el agente en tu nombre lo has hecho tú

Errores y compras incluidos: Anthropic y Google lo dicen expresamente.

---

<!-- .slide: id="que-ve" class="table" -->
## Además de lo que hace, cuenta lo que envía

| Herramienta | Qué llega al proveedor |
| --- | --- |
| Claude en Chrome | Capturas de las pestañas en las que trabaja |
| Comet | El contexto de cada petición, hasta 30 días |
| Gemini en Chrome | La pestaña actual, en la actividad de Gemini |

Notas:
Las reglas sobre datos personales son las de cualquier chatbot, con un añadido: aquí también cuenta todo lo que esté visible en pantalla.

---

<!-- .slide: id="alumnado" class="statement" -->
## Con el alumnado, mejor como objeto de estudio que como herramienta

En informática, la inyección de *prompts* es contenido de ciberseguridad.

Notas:
Claude exige 18 años y Gemini en Chrome no está disponible en España. Comet hereda los 13 años de Perplexity y ChatGPT pide consentimiento familiar a los menores de 18, pero un agente con las sesiones del alumno abiertas plantea los mismos problemas que con las tuyas.
