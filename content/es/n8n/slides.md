---
derived_from:
  es/n8n/index.md: "198118ea86e7655fc2101e5d3406c2dad0c22cdf"
---

<!-- .slide: id="receta" class="statement" -->
## Una automatización es una receta que el ordenador sigue sin ti

Un disparador y unos pasos fijos, cada vez que se dan las condiciones.

---

<!-- .slide: id="tres-formas" class="cards" -->
## *Chatbot*, automatización y agente

### *Chatbot*
Responde cuando le preguntas.

### Automatización
Siempre los mismos pasos, sin ti: predecible.

### Agente
Decide él los pasos: flexible y menos predecible.

Notas:
Una automatización puede incluir un modelo de lenguaje en un paso, e incluso un agente, pero el esqueleto lo decides tú.

---

<!-- .slide: id="herramientas" class="cards" -->
## Varias herramientas, las mismas piezas

### Zapier
Datos en Estados Unidos; su plan gratuito no admite pasos de IA.

### Make
Plan gratuito, con los datos en la UE si lo eliges al registrarte.

### n8n Cloud
Prueba gratuita; los flujos de su galería se ven sin cuenta.

### Power Automate
Incluido en las licencias educativas de Microsoft 365.

Notas:
Precios y límites, en la tabla de la página, con su fecha de revisión. Los ejemplos usan n8n, que además se puede instalar en un servidor propio. Para tareas sencillas ni siquiera hace falta un flujo: algunos asistentes, como Claude en Chrome, programan tareas periódicas.

---

<!-- .slide: id="piezas" -->
## Las piezas de un flujo

- **Disparador**: una hora, un formulario, un RSS, un correo.
- **Nodos**: cada paso recibe datos, trabaja y los pasa al siguiente.
- **Expresiones**: arrastras un dato de un paso anterior y queda como `{{ $json.title }}`.
- **Credenciales**: cuentas y claves, guardadas aparte.
- Los flujos son JSON: se copian y se pegan en el lienzo.

---

<!-- .slide: id="ejemplo-boe" class="fragments" -->
## Las novedades del BOE, resumidas cada lunes

1. Cada lunes a las 8:00.
2. Leer el RSS de «Educación y enseñanza».
3. Quedarse con las de la semana.
4. Resumir cada disposición con un modelo de lenguaje.
5. Enviarte un único correo con los enlaces.

Notas:
Un buen primer flujo: no maneja datos personales, cada resumen va con su enlace para comprobarlo y, si falla, no pasa nada grave.

---

<!-- .slide: id="demo-boe" class="demo" -->
## Un primer flujo, nodo a nodo

El boletín del BOE, viendo qué sale de cada paso.

Notas:
**Demo (12 min)**. Una cuenta de prueba de n8n Cloud, creada pocos días antes de la sesión.

1. Crear el *Schedule Trigger* y el nodo *RSS Read* con la dirección del canal.
2. Ejecutar el RSS y enseñar los elementos que salen.
3. Añadir el nodo de modelo de lenguaje con las instrucciones de la página y la expresión del título.
4. Enviar el correo a una cuenta de pruebas.

**Resultado esperado:** un correo con los resúmenes y sus enlaces.
**Si falla:** enseñar la salida de cada nodo, que es lo que explica cómo viajan los datos. Sin cuenta, recorrer el flujo de ejemplo de la galería que enlaza la página.
**Mensaje clave:** cada nodo recibe elementos y los pasa al siguiente; el esqueleto lo decides tú.

---

<!-- .slide: id="agente-en-flujo" class="statement" -->
## Un agente dentro de un flujo trae consigo los riesgos de los agentes

Leer correos de cualquiera y poder enviarlos es la tríada letal completa.

---

<!-- .slide: id="aprobacion" class="statement" -->
## Aprobación humana antes de enviar, publicar o borrar

n8n detiene el flujo hasta que alguien aprueba o rechaza la acción.

---

<!-- .slide: id="que-automatizar" class="table" -->
## Qué automatizar en un centro

| Qué | Cómo |
| --- | --- |
| Boletines, recordatorios, avisos | Adelante |
| Datos del alumnado o las familias | Solo en herramientas que autorice la administración |
| Decisiones sobre el alumnado | No, sin revisión humana |

---

<!-- .slide: id="ejecuciones" class="statement" -->
## n8n Cloud guarda los datos de cada ejecución

Lo que pasó por cada nodo queda guardado durante el tiempo que fije tu plan.

Notas:
Lo que se envía al modelo de lenguaje llega a su proveedor. Un servicio de automatización con tu cuenta es, como un *chatbot* con cuenta personal, una plataforma externa: los datos del alumnado solo van a herramientas que la administración haya contratado o autorizado. Tampoco hay nodo para Moodle: conectar con su API requiere un permiso que solo da la administración del aula virtual.
