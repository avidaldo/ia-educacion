---
derived_from:
  es/n8n/index.md: "f82a359a5a1e24db1e8a4a97c3f049d69aad5ddc"
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

<!-- .slide: id="cloud-o-local" class="two-col" -->
## n8n: en la nube o en tu equipo

### n8n Cloud
De pago (desde unos 20 € al mes), sin instalación, con los datos en la UE.

### Instalado por ti
Gratuito, en tu equipo; funciona mientras esté encendido.

Notas:
Licencia *fair-code*: gratis para uso interno, personal o no comercial, pero no se puede ofrecer como servicio a terceros. No es software libre en sentido estricto.

---

<!-- .slide: id="piezas" -->
## Las piezas de un flujo

- **Disparador**: una hora, un formulario, un RSS, un correo.
- **Nodos**: cada paso recibe datos, trabaja y los pasa al siguiente.
- **Expresiones**: `{{ $json.title }}` usa un dato de un paso anterior.
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
**Demo (12 min)**. n8n instalado en local con Docker, o una prueba de n8n Cloud.

1. Crear el *Schedule Trigger* y el nodo *RSS Read* con la dirección del canal.
2. Ejecutar el RSS y enseñar los elementos que salen.
3. Añadir el nodo de modelo de lenguaje con las instrucciones de la página y la expresión del título.
4. Enviar el correo a una cuenta de pruebas.

**Resultado esperado:** un correo con los resúmenes y sus enlaces.
**Si falla:** enseñar la salida de cada nodo, que es lo que explica cómo viajan los datos.
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
| Datos del alumnado o las familias | Con mucho cuidado y con autorización del centro |
| Decisiones sobre el alumnado | No, sin revisión humana |

---

<!-- .slide: id="ejecuciones" class="statement" -->
## n8n guarda los datos de cada ejecución

Lo que pasó por cada nodo queda guardado: conviene borrar las ejecuciones antiguas automáticamente.

Notas:
Lo que se envía al modelo de lenguaje llega a su proveedor, y la responsabilidad del tratamiento es del centro. Tampoco hay nodo para Moodle: conectar con su API requiere un permiso que solo da la administración del aula virtual.

---

<!-- .slide: id="alternativas" -->
## Otras opciones

- **Zapier** y **Make**: en la nube, sin instalación propia.
- **Power Automate**, si el centro trabaja con Microsoft 365.
- Para tareas sencillas, las tareas programadas de algunos asistentes, como Claude en Chrome.
