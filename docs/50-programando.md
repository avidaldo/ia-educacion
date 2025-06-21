# Creando aplicaciones sin saber programar

## Para importar a Moodle (aulas virtuales)

### Creación de preguntas en formatos importables

- [Formato Aiken](https://docs.moodle.org/all/es/Formato_Aiken): Sencillo e interpretable, limitado (preguntas de opción múltiple sin penalización por respuesta incorrecta)
- [Formato GIFT](https://docs.moodle.org/all/es/Formato_GIFT): Más complejo, permite preguntas de opción múltiple con distinta puntuación para cada respuesta, incluyendo una respuesta correcta y una incorrecta.


### Creación de páginas en HTML

Cualquier chatbot puede crear páginas en HTML fácilmente a golpe de prompt y después darte los pasos para insertarlas en Moodle. Bastará con descargar la página y pegar el código HTML en un recurso de tipo "Página" de Moodle, o también en recurso de tipo "Etiqueta" si quieres que se vea directamente en la página de tu curso.

## Recursos para crear aplicaciones sin programación

- [Claude Artifacts](https://claude.ai/artifacts): Crear aplicaciones simples con IA y publicarlas gratuitamente
  - **Guía rápida**: 
    1. Visita Claude.ai y accede con tu cuenta
    2. En la sección Artifacts, describe la aplicación que necesitas
    3. Claude la creará automáticamente y te dará un enlace para compartir. Almacenará el código en su servidor.

:::note[Artículo interesante]
[Cómo crear mini-aplicaciones educativas con Claude](https://educacion.bilateria.org/como-crear-aplicaciones-educativas-con-claude)
:::

### Integrar aplicaciones en Moodle

Para insertar una aplicación (como un Claude Artifact) en Moodle:

#### Usando la URL de la aplicación

Puedes usar la URL (el enlace de Claude Artifacts) para insertarla en Moodle directamente con un recurso de tipo "URL".

#### Usando un iframe

1. Obtén el enlace de tu aplicación (por ejemplo, el enlace de Claude Artifacts)
2. En tu curso de Moodle, activa el modo de edición
3. Añade un recurso o actividad del tipo "Página" o "Etiqueta"
4. Haz clic en el icono de código HTML `<>`
5. Pega un código iframe como el siguiente:
   ```
   <iframe src="https://tu-enlace-de-aplicacion" width="100%" height="600px" frameborder="0"></iframe>
   ```
6. Guarda los cambios


