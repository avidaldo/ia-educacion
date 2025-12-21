# Chatbots y herramientas

![](./img/herramientas_napkin.png)  

(imagen creada con Napkin partiendo de estos mismos apuntes)

## Chatbots (LLMs)

### OpenAI

- [ChatGPT](https://chat.openai.com/) - GPT-5.2, GPT-5.2 Pro, GPT-5.2-Codex
  - Anterior: GPT-5, GPT-5.1, GPT-4o
  - Modelos razonadores: integrados en GPT-5.x (razonamiento interno automático)

Integra:
- Dall-E: texto a imagen
- Sora: texto a vídeo

- [GPTs personalizados](https://chatgpt.com/gpts): asistentes con prompts específicos para tareas concretas.

### Google

- [Gemini](https://gemini.google.com/) - Gemini 3 Pro, Gemini 3 Flash
  - Anterior: Gemini 2.5 Pro, Flash
  - Gemini 3 Deep Think: modo de razonamiento mejorado
  - Integrado con Gmail, GDocs, GMaps, **YouTube**...
  - [Gems](https://gemini.google.com/gems): asistentes personalizados (equivalente a GPTs)
  - Chatbot educativo con Google Workspace for Education

- [NotebookLM](https://notebooklm.google/) - ver [sección dedicada](./22-notebooklm.md)
  - IA "source-grounded": solo responde basándose en tus documentos
  - Genera podcasts, guías de estudio, quizzes...

- [AI Studio](https://aistudio.google.com/)
  - Modelos experimentales (2.5 Flash) y personalización técnica avanzada
  - Streaming en tiempo real (IA asistiendo a vídeo)

### [Claude](https://claude.ai/) (Anthropic)
- Claude Opus 4.5 (modelo más capaz, noviembre 2025)
- Claude Sonnet 4.5 (septiembre 2025)
  - Anteriores: Claude 3.5 Sonnet, Claude 3 Opus
- Líder en programación, agentes y uso de ordenador
- [Claude Artifacts](https://claude.ai/artifacts): crea y publica aplicaciones directamente

### [DeepSeek](https://chat.deepseek.com/)
- **DeepSeek-R1**: modelo razonador que compite con o1 en benchmarks, 27 veces más barato
- *Open weights* (podemos descargarlo, ver cómo funciona, crear nuestra versión...)
- Permite ver la cadena de pensamiento (CoT) completa

### Grok (xAI)
- [Grok](https://x.com/i/grok?focus=1) - Integrado en X (Twitter)

### [Copilot](https://copilot.microsoft.com/) (Microsoft)
- Basado en GPT-4o
- Copilotos integrados en Office 365, Teams, etc.

### [Le Chat](https://chat.mistral.ai/chat) (Mistral)
- Único competidor europeo relevante (francés, *open weights*)

### [Qwen](https://chat.qwenlm.ai/) 
- Modelo chino (*open weights*), muy competitivo


## Configuración de Chatbots

### Memoria

Los chatbots modernos pueden recordar información entre conversaciones:

| Chatbot | Característica | Descripción |
|---------|---------------|-------------|
| **ChatGPT** | Memory | Recuerda preferencias y datos entre chats. Activable/desactivable. |
| **Gemini** | Memory | Recuerda contexto de conversaciones previas. Configurable. |
| **Claude** | Projects | Organiza conversaciones con contexto compartido. |

### Chats Temporales (Privacidad)

Para conversaciones que no quieres que queden guardadas ni entrenen al modelo:

- **ChatGPT**: *Temporary Chat* - se borra automáticamente tras 30 días, no entrena el modelo
- **Gemini**: *Chat temporal* - se borra tras 72 horas, no entrena el modelo, similar al modo incógnito
- **Claude**: Opción de no compartir datos para entrenamiento

> [!TIP]
> Usa chats temporales cuando trabajes con información sensible o confidencial.

### Canvas / Espacios de Trabajo

Interfaces avanzadas para edición colaborativa con la IA:

**ChatGPT Canvas** ([documentación](https://openai.com/index/introducing-canvas/)):
- Panel de chat + editor integrado
- Edición inline: selecciona texto y pide cambios específicos
- Para código: depuración, comentarios, refactoring, ejecución de Python
- Para texto: ajustar nivel de lectura, expandir/contraer, revisar gramática
- Control de versiones: deshacer cambios, restaurar versiones anteriores

**Gemini** también permite editar código y documentos de forma colaborativa, aunque con menos funcionalidades que Canvas.


## Navegadores con IA

Nueva categoría de navegadores que integran IA para automatizar tareas:

### [Dia Browser](https://diabrowser.com/) (The Browser Company)
- Navegador "AI-first" de los creadores de Arc
- Chatbot integrado que accede a información de todas las pestañas abiertas
- Barra de direcciones conversacional
- Sistema de "Skills" para guardar prompts frecuentes
- Automatización de tareas online

### [Perplexity Comet](https://www.perplexity.ai/)
- Navegador de Perplexity con búsqueda integrada
- Investigación en profundidad mientras navegas

### Otros navegadores con IA
- **Microsoft Edge** con Copilot integrado
- **Brave Leo**: asistente IA privado
- **Opera Aria**: asistente con acceso a información actualizada


## Otras herramientas

### [Perplexity](https://www.perplexity.ai/)

- Permite usar modelos como los anteriores pero para buscar en la web
- Permite realizar investigaciones en profundidad, parecido a *Deep Research* de ChatGPT pero mucho más rápido

### [Mermaid](https://mermaid.js.org/)
- Genera diagramas de flujo, secuencias, etc. desde texto

- GPT's específicos:
    - [Oficial de Mermaid](https://chatgpt.com/g/g-1IRFKwq4G-mermaid-chart-diagrams-and-charts)
    - [Sonia (genera el código y enseña a insertarlo)](https://chatgpt.com/g/g-7BAVTYCJr-sonia-diagramas-educativos-mermaid)


### [Video Highlight](https://videohighlight.com/)
- Transcribe y resume vídeos y permite chatear sobre el contenido


### Herramientas para crear presentaciones

Ver [sección dedicada a presentaciones con IA](./23-presentaciones.md)

- [Gamma](https://gamma.app/) - Generación rápida con IA
- [Canva](https://www.canva.com/education/) - Control de diseño extenso
- [Beautiful.AI](https://www.beautiful.ai/)
- [slidesgpt](https://slidesgpt.com)


### Especialmente para el ámbito educativo

- [Magic School](https://www.magicschool.ai/)
- [Poe AI](https://poe.com)
- [unstuckstudy](https://unstuckstudy.com)


## Detección de plagio

- [zerogpt](https://www.zerogpt.com/)
- [Turnitin](https://www.turnitin.com/)
- [Quibot](https://quillbot.com/ai-content-detector)
- [Grammarly](https://www.grammarly.com/plagiarism-checker)
- [Plagiarism Checker](https://www.plagiarismchecker.com/)


## Modelos de texto a imagen

- Dall-E - Integrado en ChatGPT
- Gemini (Imagen 3)
- Grok (Flux)
- [Midjourney](https://www.midjourney.com)
- [Adobe Firefly](https://firefly.adobe.com/)
- [Stable Diffusion](https://stability.ai/stable-assistant) / [Flux](https://flux-ai.io/)
- [Ideogram](https://ideogram.ai/)
- [Leonardo](https://app.leonardo.ai/)
- [NightCafé](https://nightcafe.ai/)
- [Freepik](https://www.freepik.com/)
- [LogoMaker](https://www.logomaker.com/) (Para logos)
