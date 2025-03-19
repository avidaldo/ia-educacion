---
sidebar_position: 5
---

# Creando Aplicaciones sin Programación

## Moodle

### Creación de preguntas en formatos importables

- [Formato GIFT](https://docs.moodle.org/all/es/Formato_GIFT): Formato de texto para crear preguntas importables
  - Puedes generar estas preguntas con ChatGPT u otros asistentes de IA
  
- [Formato Aiken](https://docs.moodle.org/all/es/Formato_Aiken): Formato simple para preguntas de opción múltiple
  - Estructura sencilla ideal para generar con herramientas de IA

- [H5P](https://h5p.org/): Contenido interactivo importable en Moodle
  - Presentaciones, cuestionarios, líneas de tiempo, etc.
  - Interfaz visual sin necesidad de programación

### Creación de páginas en HTML

Cualquier chatbot puede crear páginas en HTML fácilmente a golpe de prompt y después darte los pasos para insertarlas en Moodle.


## Recursos para crear sin programación

- [Claude Artifacts](https://claude.ai/artifacts): Crear aplicaciones simples con IA y publicarlas gratuitamente
  - **Guía rápida**: 
    1. Visita Claude.ai y accede con tu cuenta
    2. En la sección Artifacts, describe la aplicación que necesitas
    3. Claude la creará automáticamente y te dará un enlace para compartir
    4. Puedes insertar este enlace en Moodle usando un iframe

### Incrustar aplicaciones en Moodle

Para insertar una aplicación (como un Claude Artifact) en Moodle:

1. Obtén el enlace de tu aplicación (por ejemplo, el enlace de Claude Artifacts)
2. En tu curso de Moodle, activa el modo de edición
3. Añade un recurso o actividad del tipo "Página" o "Etiqueta"
4. Haz clic en el icono de código HTML `<>`
5. Pega un código iframe como el siguiente:
   ```
   <iframe src="https://tu-enlace-de-aplicacion" width="100%" height="600px" frameborder="0"></iframe>
   ```
6. Guarda los cambios


