# AGENTS.md

## Contexto del proyecto

Web educativa dirigida a **docentes de educación secundaria** que quieren comprender las herramientas de IA y sus casos de uso aplicados a la docencia. El objetivo no es formar expertos técnicos, sino dar una comprensión práctica y fundamentada de estas tecnologías.

## Tono y enfoque del contenido

- **Audiencia**: Profesorado de secundaria, sin conocimientos técnicos previos en IA.
- **Lenguaje divulgativo**: Usar términos accesibles (ej: "agente de IA" en lugar de "LLM" o "modelo de lenguaje"). Evitar jerga técnica innecesaria; cuando sea imprescindible un término técnico, explicarlo brevemente.
- **Sin promoción de herramientas comerciales**: No favorecer ni recomendar herramientas específicas (ChatGPT, Gemini, Claude, etc.). Mantener un enfoque neutral y centrado en conceptos.
- **Nivel de profundidad adecuado**: Explicar conceptos a nivel funcional (qué hacen, para qué sirven) sin entrar en arquitectura interna (ej: no explicar transformers, attention, etc.).
- **Perspectiva científica**: Priorizar siempre la comprensión basada en evidencia.
- **No antropomorfizar las IAs**: Evitar atribuir intenciones, emociones o agencia a los modelos. Son herramientas estadísticas, no entidades.
- **No criminalizar las IAs**: Los sesgos y problemas éticos deben explicarse desde la comprensión técnica (datos de entrenamiento, diseño, limitaciones), no desde el sensacionalismo ni el miedo.
- **Ética basada en comprensión**: El uso ético y correcto de la IA debe fundamentarse en el análisis crítico de la realidad, no en prohibiciones o miedos infundados.
- El contenido se escribe en **español**.

## Traducciones (i18n)

El proyecto tiene traducciones a **gallego, inglés e italiano** en el directorio `i18n/`. Al editar contenido en `docs/`:

- **No traducir automáticamente** cada cambio intermedio para ahorrar tokens.
- Al terminar de editar un documento, **recordar al usuario** que existen traducciones que pueden necesitar sincronización.
- Cuando el usuario lo pida, usar `git diff` sobre el archivo modificado para identificar exactamente qué cambió y aplicar solo esos cambios en la traducción correspondiente. Esto evita tener que releer el documento completo y también identifica cambios de estructura (ficheros movidos o nuevos creados).

## Comandos de desarrollo

- Se requiere **Node.js ≥ 20.0**
- Instalar dependencias: `npm ci`
- Servidor de desarrollo: `npm start`
- Build de producción: `npm run build`
- Comprobación de tipos: `npm run typecheck`
- Limpiar caché: `npm run clear`

## Cómo añadir y editar contenido

- Los documentos van en `docs/` como archivos `.md` o `.mdx`, ordenados con prefijo numérico (ej: `10-historia-y-llms.md`).
- Cada documento necesita frontmatter con `sidebar_position` y `title`.
- El sidebar se auto-genera desde la estructura de `docs/`.

### Conversaciones de chat con IA

Para mostrar ejemplos de conversaciones, crear un archivo YAML en `static/data/chats/`:

```yaml
model: "Asistente IA"   # Opcional
date: "2024-12-21"      # Opcional
messages:
  - role: user
    content: Tu pregunta aquí
  - role: assistant
    content: |
      Respuesta con soporte de **markdown**.
```

Y referenciarlo en MDX:

```mdx
import { ChatConversation } from '@site/src/components/ChatConversation';

<ChatConversation source="/data/chats/ejemplo.yaml" />
```

#### Traducción de chats

Los archivos YAML de `static/data/chats/` son el contenido por defecto (español). Para traducir un chat a otro idioma, crear el mismo archivo en `i18n/{locale}/chat-data/`:

```
i18n/en/chat-data/specific-role.yaml   ← traducción al inglés
i18n/gl/chat-data/specific-role.yaml   ← traducción al gallego
i18n/it/chat-data/specific-role.yaml   ← traducción al italiano
```

- Solo es necesario crear los archivos que se quieran traducir; los que no existan usarán el contenido por defecto en español.
- El nombre del archivo debe coincidir exactamente con el original en `static/data/chats/`.
- El formato del YAML traducido es idéntico al original.

## Estilo de código

- TypeScript con anotaciones de tipo. Componentes funcionales de React.
- CSS Modules (`.module.css`) para estilos de componentes.
- La base URL es `/ia-educacion/` — las rutas de assets deben tenerlo en cuenta.
- No modificar `build/`, `node_modules/` ni `.docusaurus/`.
