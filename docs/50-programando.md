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

## De Vibe Coding a agentes (automatización con criterios)

El vibe coding suele describirse como “iterar por sensación” hasta que algo funciona. Eso es útil para prototipos, pero en cuanto quieres **fiabilidad**, conviene pasar de “chat” a un **flujo tipo agente**.

### Qué es un agente (en la práctica)

Un agente no es “una IA más lista”, sino un sistema que:

- persigue un **objetivo** (con criterios de aceptación),
- mantiene **estado** (qué se intentó, qué falló, qué queda),
- puede usar **herramientas** (tests, linters, búsqueda, conversores de formato, etc.),
- ejecuta un bucle controlado y **se detiene** cuando cumple el objetivo.

Si quieres ver plantillas orientadas a docencia, aquí tienes ejemplos listos para reutilizar:

- [/docs/ejemplos/agentes-y-orquestacion](/docs/ejemplos/agentes-y-orquestacion)
- [/docs/ejemplos/razonamiento-avanzado](/docs/ejemplos/razonamiento-avanzado)

### Patrones que funcionan (y cómo pedirlos)

**1) Planner/Executor (planificar → ejecutar → validar)**

- Pide un plan corto (3–7 pasos), luego ejecución paso a paso con validación.
- Define una “Definition of Done”: qué pruebas pasar, qué archivos cambiar, qué formato entregar.

**2) Critique loop (borrador → crítica → versión final)**

- Útil para: rúbricas, actividades, bancos de preguntas, textos explicativos.
- Limita rondas (1–2) y define criterios (claridad, privacidad, verificabilidad).

**3) Tool-use / ReAct (Acción → Observación → Ajuste)**

- Útil para: investigación con fuentes, verificación, extracción y re-formateo.
- Pide “acciones y observaciones” (qué hizo y qué obtuvo). Evita pedir “pensamiento paso a paso”.

**4) Multi‑agente (roles: diseñar → evaluar → editar)**

- Útil cuando quieres separar creatividad, revisión crítica y edición final.
- Define roles y orden estricto para reducir el sesgo de auto‑confirmación.

### Prompts más útiles al programar con IA

Cuando uses Copilot/Cursor/Canvas/Artifacts, estos requisitos suelen mejorar mucho la calidad:

- Entradas/salidas como contrato: “devuélveme solo el código”, “encabezados fijos”, “tabla con columnas X”.
- Criterios de parada: “para cuando pase X / cuando no haya warnings / cuando compile”.
- Restricciones: “no añadir dependencias”, “no inventar datos”, “no usar datos personales”.

Para la base de prompting (formato, delimitadores, verificación), ver: [/docs/prompt](/docs/prompt)

### Fuentes (fiables) para el concepto de agente

- ReAct (Reasoning + Acting): https://arxiv.org/abs/2210.03629
- Reflexion (agentes con feedback/memoria): https://arxiv.org/abs/2303.11366
- Self-Refine (mejora iterativa con auto-feedback): https://arxiv.org/abs/2303.17651
- AutoGen (multi‑agente): https://arxiv.org/abs/2308.08155
- MetaGPT (multi‑agente): https://arxiv.org/abs/2308.00352

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
