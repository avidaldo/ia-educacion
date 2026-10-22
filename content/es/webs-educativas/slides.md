---
derived_from:
  es/webs-educativas/index.md: "738bad2789a5baa7ac8e4bee0f328d088d2bf28b"
  es/webs-educativas/presentaciones.md: "8ba1f937e70def616ac39f15221015ce5d2889c5"
---

<!-- .slide: id="sin-programar" class="statement" -->
## Una página interactiva para clase, sin saber programar

Simuladores, repasos, líneas de tiempo, juegos: un único fichero HTML.

---

<!-- .slide: id="ejemplos" class="fragments" -->
## Lo que funciona bien

- Un simulador sencillo.
- Un repaso con pistas y corrección inmediata.
- Una línea de tiempo o un mapa que se explora con clics.
- Una calculadora de la materia.
- Un juego de vocabulario o de emparejar conceptos.

---

<!-- .slide: id="donde-crear" class="table dense" -->
## Dónde crearlas

| Herramienta | Compartir el resultado |
| --- | --- |
| Claude (Artifacts) | Quien la abra necesita cuenta de Claude (18 años) |
| Gemini (Canvas) | Enlace público; quien lo tenga puede editar los datos de la aplicación |
| ChatGPT (Canvas) | Descargar el código y publicarlo fuera |

Notas:
En todos los casos, lo más robusto es pedir un único fichero HTML, descargarlo y publicarlo tú donde ya entra el alumnado.

---

<!-- .slide: id="prompt-pagina" class="prompt dense" -->
## Cómo pedirla

```text
Crea una página web interactiva en un único fichero HTML, sin dependencias externas,
para [nivel] sobre [tema].
Debe permitir: [lo que hará el alumnado, paso a paso].
Diseño legible en móvil y proyector, buen contraste, manejable con teclado.
No recojas ni envíes ningún dato del usuario.
```

---

<!-- .slide: id="demo-pagina" class="demo" -->
## Del encargo a Moodle

Crear, iterar y publicar una página en diez minutos.

Notas:
**Demo (10 min)**. Gemini (Canvas) o Claude, y un curso de pruebas de Moodle.

1. Pedir una página con el *prompt* de la página y un tema propuesto por el grupo.
2. Probarla y pedir dos cambios concretos («añade una pista en cada pregunta»).
3. Descargar el fichero HTML.
4. Crear un recurso Página en Moodle y pegar el código en la vista de código.

**Resultado esperado:** la página funciona dentro de Moodle.
**Si falla:** si Moodle borra el código, subir el fichero como recurso Archivo.
**Mensaje clave:** el contenido se revisa como cualquier material; el diseño es lo fácil.

---

<!-- .slide: id="moodle" class="table" -->
## Publicarla en Moodle

| Opción | Cuándo |
| --- | --- |
| Recurso Página, pegando el HTML | Lo más sencillo |
| Área de texto y medios con un `<iframe>` | Para verla en la portada del curso |
| Recurso Archivo con el `.html` | Si Moodle borra el código |
| Recurso URL | Si ya está publicada fuera |

Notas:
Moodle limpia el HTML en la mayoría de sitios (los foros, por ejemplo), pero no en el recurso Página ni en las descripciones como el área de texto y medios, salvo que la administración haya activado la limpieza en todo el sitio.

---

<!-- .slide: id="fuera" class="two-col" -->
## Publicarla fuera de Moodle

### Netlify Drop
Arrastras la carpeta y obtienes una dirección pública.

### GitHub Pages
Gratuito y estable; así se publica esta web.

---

<!-- .slide: id="revisar" class="checklist" -->
## Antes de publicar

- [ ] Contenido correcto.
- [ ] Funciona en móvil, ordenador y proyector.
- [ ] Accesible: contraste, teclado, textos alternativos.
- [ ] No recoge datos ni carga recursos de otras webs.
- [ ] Imágenes propias o con licencia.

---

<!-- .slide: id="presentaciones" class="section" -->
## Presentaciones

---

<!-- .slide: id="contenido-primero" class="statement" -->
## Primero el esquema; después el diseño

Pedir de golpe «una presentación sobre X» da diapositivas vistosas con contenido genérico.

---

<!-- .slide: id="tres-caminos" class="cards" -->
## Tres caminos

### *Chatbot*
Gemini (Canvas, a Google Slides), cuadernos, ChatGPT y Claude (PowerPoint).

### Herramienta especializada
Gamma o Canva: el resultado más vistoso, en su plataforma.

### Texto y estilo
Markdown convertido con Marp, Slidev o reveal.js: contenido reutilizable, diseño fijo.

---

<!-- .slide: id="practica-presentacion" class="practice" -->
## Del esquema a las diapositivas

1. Pide un esquema de diez diapositivas sobre un tema de tu materia.
2. Corrígelo: datos, orden, lo que sobra.
3. Genera las diapositivas por uno de los tres caminos.
4. Revisa lo que cambió entre el esquema y el resultado.

**15 minutos.** Producto: una presentación con contenido revisado.
