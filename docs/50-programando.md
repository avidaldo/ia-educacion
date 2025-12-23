# Creando aplicaciones sin saber programar

## Vibe Coding

**Vibe coding** es un término acuñado por [Andrej Karpathy](https://twitter.com/karpathy) en febrero de 2025 para describir una nueva forma de programar donde la IA genera el código y el humano lo guía mediante prompts en lenguaje natural.

> "The hottest new programming language is English" — Andrej Karpathy

### ¿Cómo funciona?

1. **Describes** lo que quieres en lenguaje natural
2. La IA **genera** el código
3. **Ejecutas** y observas el resultado
4. **Iteras** con correcciones hasta conseguir lo deseado

### Herramientas para Vibe Coding

| Herramienta | Descripción |
|-------------|-------------|
| **Claude Artifacts** | Crea aplicaciones web y las aloja automáticamente |
| **ChatGPT Canvas** | Espacio de trabajo con edición y ejecución de código |
| **Gemini** | Genera código con posibilidad de exportar |
| **Cursor / GitHub Copilot** | Editores de código con IA integrada |

### Ventajas
- ✅ No necesitas saber programar para crear aplicaciones simples
- ✅ Prototipado muy rápido
- ✅ Ideal para herramientas educativas pequeñas

### Limitaciones
- ⚠️ El código puede tener errores o vulnerabilidades
- ⚠️ Difícil de mantener si no entiendes el código
- ⚠️ Mejor para prototipos que para producción

---

## Espacios de trabajo en chatbots

### Claude Artifacts

[Claude Artifacts](https://claude.ai/artifacts) permite crear y publicar aplicaciones web directamente desde el chat.

**Guía rápida**: 
1. Visita [Claude.ai](https://claude.ai/) y accede con tu cuenta
2. Describe la aplicación que necesitas
3. Claude la crea automáticamente y te da un enlace para compartir
4. El código se aloja en los servidores de Anthropic

:::note[Artículo interesante]
[Cómo crear mini-aplicaciones educativas con Claude](https://educacion.bilateria.org/como-crear-aplicaciones-educativas-con-claude)
:::

**Ejemplos de uso educativo**:
- Calculadoras interactivas
- Quizzes y juegos educativos
- Visualizaciones de conceptos
- Simuladores simples

### ChatGPT Canvas

[Canvas](https://openai.com/index/introducing-canvas/) es el espacio de trabajo de ChatGPT para proyectos más elaborados.

**Características**:
- Panel de chat + editor integrado
- **Edición inline**: selecciona código y pide cambios específicos
- **Ejecución de Python**: ejecuta código directamente
- **Control de versiones**: deshacer cambios, restaurar versiones
- **Herramientas de código**: depurar, comentar, refactorizar, traducir a otros lenguajes

**Cómo activarlo**:
- Automáticamente cuando detecta código largo
- Manualmente escribiendo "usa canvas" o "abre un canvas"

### Gemini

Gemini también puede generar código y aplicaciones, aunque con menos capacidad de hosting directo. Sin embargo, permite:
- Generar código en múltiples lenguajes
- Colaborar en la edición
- Exportar para usar en otros sitios

---

## Integrar aplicaciones en Moodle

Para insertar una aplicación (como un Claude Artifact) en Moodle:

### Usando la URL de la aplicación

Puedes usar la URL (el enlace de Claude Artifacts) para insertarla en Moodle directamente con un recurso de tipo "URL".

### Usando un iframe

1. Obtén el enlace de tu aplicación
2. En tu curso de Moodle, activa el modo de edición
3. Añade un recurso o actividad del tipo "Página" o "Etiqueta"
4. Haz clic en el icono de código HTML `<>`
5. Pega un código iframe:
   ```html
   <iframe src="https://tu-enlace-de-aplicacion" width="100%" height="600px" frameborder="0"></iframe>
   ```
6. Guarda los cambios

### Creación de páginas HTML

Cualquier chatbot puede crear páginas HTML fácilmente a golpe de prompt. Después puedes:
- Descargar la página y pegar el código en un recurso "Página" de Moodle
- Usar un recurso "Etiqueta" para que se vea directamente en la página del curso

---

## Recursos relacionados

- [Tests para Moodle](./51-tests-moodle.mdx) - Generación de preguntas importables
- [Asistentes personalizados](./31-ejemplos/09-asistente-personalizado.mdx) - Crear GPTs y Gems
