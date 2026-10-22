---
title: Webs educativas
description: Crear con IA pequeñas páginas interactivas para clase (simuladores, repasos, juegos) y publicarlas donde el alumnado pueda usarlas.
reviewed: 2026-10-22
review_every: 3
---

## Qué se puede crear

Con una descripción en lenguaje natural, los *chatbots* generan **páginas web interactivas** que funcionan en el navegador: no hace falta saber programar para obtener un primer resultado útil. Algunos ejemplos que funcionan bien en clase:

- un simulador sencillo (un circuito, un plano inclinado, una economía con dos variables);
- un repaso interactivo con preguntas, pistas y corrección inmediata;
- una línea de tiempo o un mapa conceptual que se explora con clics;
- una calculadora específica de la materia (escalas, porcentajes, unidades);
- un juego de vocabulario o de emparejar conceptos.

Una página así es un único fichero HTML con su diseño y su código. Cuando el proyecto crece (varias pantallas, datos guardados, usuarios), ya no es una página sino una aplicación: se trata en [*Vibe coding*](../vibe-coding/index.md).

## Dónde crearlas

| Herramienta | Cómo se crea | Compartir el resultado |
| --- | --- | --- |
| Claude | Los Artifacts muestran la página funcionando junto al chat | Con enlace, pero **quien la abra necesita cuenta de Claude** (y Claude exige 18 años). Para el alumnado, descarga el código y publícalo en otro sitio |
| Gemini | Canvas, también en el plan gratuito | Con un enlace público que se abre en gemini.google.com. Según Google, quien tenga el enlace puede ver y editar los datos asociados a la aplicación |
| ChatGPT | Canvas para código y, desde GPT-6, respuestas con elementos interactivos. En los planes Plus y Pro, Sites (en pruebas) crea y publica páginas y aplicaciones ligeras | Con Sites, con una dirección propia; si no, descarga el código para publicarlo fuera de ChatGPT |

En todos los casos, el camino más robusto es el mismo: **pedir la página como un único fichero HTML, descargarlo y publicarlo tú** donde el alumnado ya entra.

## Cómo pedirla

```text
Crea una página web interactiva en un único fichero HTML, sin dependencias externas
(nada de CDN, fuentes ni imágenes de otras webs), para [nivel] sobre [tema].

Debe permitir: [lo que hará el alumnado, paso a paso].
Diseño: claro y legible en móvil y en el proyector, con buen contraste,
manejable con teclado y con textos alternativos en las imágenes.
Idioma: [castellano / gallego].
No recojas ni envíes ningún dato del usuario.
Al final, explica en tres líneas cómo se usa.
```

Después, itera como con cualquier otro texto: prueba la página, describe lo que falla o lo que quieres cambiar («el botón de comprobar no reinicia las respuestas», «añade una pista en cada pregunta») y pide la versión corregida completa.

> [!TIP]
> **Contenido primero, diseño después**
> Si la página explica algo, revisa primero el contenido (en texto, o en un diagrama Mermaid) y pide después la página con ese contenido ya validado. Mezclar en una sola petición el razonamiento y el diseño aumenta los errores, como se explica en [Técnicas avanzadas](../prompts/avanzado.md#separar-contenido-y-diseño).

## Publicarla en Moodle

| Opción | Cómo | Cuándo usarla |
| --- | --- | --- |
| Recurso **Página** | Pega el HTML en la vista de código del editor | Lo más sencillo para una página autocontenida |
| **Área de texto y medios** (antes «Etiqueta») | Inserta un `<iframe>` que apunte a la página publicada en otro sitio | Para que se vea directamente en la portada del curso |
| Recurso **Archivo** | Sube el fichero `.html` | Si prefieres que se abra en una pestaña aparte |
| Recurso **URL** | Enlaza la página publicada fuera de Moodle | Si ya está alojada en otra web |

Un `<iframe>` tiene esta forma:

```html
<iframe src="https://direccion-de-tu-pagina" width="100%" height="600" title="Simulador de circuitos"></iframe>
```

> [!NOTE]
> **Por qué a veces Moodle borra el código**
> Moodle «limpia» el HTML que se escribe en la mayoría de sitios (por ejemplo, en los foros) y elimina los `<iframe>` y el código. El contenido de un recurso **Página** y las descripciones de recursos y actividades, como el área de texto y medios, se muestran sin limpiar, así que ahí funcionan. La excepción es que la administración del sitio haya activado la limpieza de contenido en todo el sitio: en ese caso, la opción que queda es el recurso **Archivo** o un enlace.

## Publicarla fuera de Moodle

- **[Netlify Drop](https://app.netlify.com/drop)**: arrastras la carpeta con la página y obtienes una dirección pública en segundos.
- **[GitHub Pages](https://pages.github.com)**: gratuito y estable para quien ya usa GitHub; es como se publica esta misma web.
- **Google Sites** permite insertar código HTML en una página del sitio.

Una vez publicada, la dirección se puede enlazar desde Moodle o insertar con un `<iframe>`.

## Antes de publicarla

- [ ] **El contenido es correcto**: revisa datos, fórmulas y textos como revisarías cualquier material.
- [ ] **Funciona** en el móvil, en el ordenador del aula y en el proyector.
- [ ] **Es accesible**: contraste suficiente, manejable con teclado, textos alternativos.
- [ ] **No recoge datos** ni carga recursos de otras webs (fuentes, analíticas, CDN), que enviarían información del alumnado a terceros.
- [ ] **Las imágenes** son propias o tienen una licencia que permita usarlas.
