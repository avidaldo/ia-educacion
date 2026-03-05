# AGENTS.md

Web educativa construida con Docusaurus sobre el uso de herramientas de IA en la docencia ("Docencia con IA").
El contenido está escrito principalmente en español, con soporte de traducción al gallego.

## Comandos de configuración

- Se requiere **Node.js ≥ 20.0**
- Instalar dependencias: `npm ci`
- Servidor de desarrollo: `npm start` (o `npm run dev`)
- Build de producción: `npm run build`
- Servir build de producción: `npm run serve`
- Comprobación de tipos TypeScript: `npm run typecheck`
- Limpiar caché de Docusaurus: `npm run clear`

## Stack tecnológico

- **Docusaurus v3.9.2** (generador de sitios estáticos)
- **React 18** con **TypeScript**
- **MDX** para páginas de contenido (Markdown + JSX)
- Búsqueda local con `@easyops-cn/docusaurus-search-local` (idioma español)
- Despliegue en GitHub Pages (GitHub Actions al hacer push a `master`)

## Estructura del proyecto

```
docs/                    → Contenido de documentación (archivos Markdown/MDX)
src/
  components/            → Componentes React
    ChatConversation/    → Componente personalizado para renderizar conversaciones de IA
    HomepageFeatures/    → Tarjetas de la página principal
  css/                   → Hojas de estilo personalizadas
  pages/                 → Páginas personalizadas (inicio, presentación)
static/
  data/chats/            → Archivos YAML con datos de conversaciones
plugins/
  chat-data-plugin.js    → Plugin personalizado de Docusaurus (carga YAML en build)
docusaurus.config.ts     → Configuración principal de Docusaurus
sidebars.ts              → Estructura del sidebar (auto-generada desde docs/)
.github/workflows/       → CI/CD (deploy.yml, test-deploy.yml)
i18n/                    → Archivos de internacionalización (traducciones al gallego)
```

## Directrices de contenido

- Toda la documentación va en `docs/` como archivos `.md` o `.mdx`.
- Los archivos se ordenan con prefijo numérico (ej: `10-historia-y-llms.md`, `20-herramientas.md`).
- El contenido se escribe en **español**. Usar lenguaje claro y educativo, apropiado para docentes que aprenden sobre IA.
- Cada archivo de documentación debe incluir frontmatter con al menos `sidebar_position` y `title`.
- Los archivos MDX pueden importar componentes React (ej: `ChatConversation`).

## Sistema de conversaciones de chat

El proyecto tiene un sistema personalizado para mostrar conversaciones de chat con IA:

1. **Archivos YAML** en `static/data/chats/` con este formato:
   ```yaml
   model: "GPT-4"       # Opcional
   date: "2024-12-21"   # Opcional
   messages:
     - role: user
       content: Tu pregunta aquí
     - role: assistant
       content: |
         Respuesta de la IA con soporte de **markdown**.
   ```

2. **Carga en tiempo de build**: El plugin `plugins/chat-data-plugin.js` carga todos los YAML durante el build (sin peticiones en tiempo de ejecución). Un YAML inválido hará fallar el build intencionadamente.

3. **Uso en MDX**:
   ```mdx
   import { ChatConversation } from '@site/src/components/ChatConversation';

   <ChatConversation source="/data/chats/ejemplo-chat.yaml" />
   ```

## Estilo de código

- TypeScript para configuración y componentes; usar anotaciones de tipo adecuadas.
- Solo componentes funcionales de React (no componentes de clase).
- CSS Modules para estilos de componentes (`.module.css`).
- Seguir las convenciones de Docusaurus para temas y plugins.
- CommonJS (`require`) en el archivo del plugin (`chat-data-plugin.js`); ESM/TypeScript en el resto.

## Despliegue

- **Automático**: Push a `master` dispara GitHub Actions → build → despliegue en rama `gh-pages`.
- **Manual**: `npm run deploy` (requiere permisos de GitHub).
- La base URL es `/ia-educacion/` — todos los assets y enlaces deben tener esto en cuenta.

## Internacionalización (i18n)

- Locale por defecto: `es` (español)
- Locale adicional: `gl` (gallego)
- Las traducciones están en el directorio `i18n/`.
- El sistema i18n de Docusaurus gestiona el cambio de idioma.

## Notas importantes

- El sidebar se **auto-genera** desde la estructura del directorio `docs/`. No se necesitan entradas manuales.
- Las imágenes referenciadas en contenido YAML de chats deben usar rutas relativas a la raíz del sitio (ej: `/img/ejemplo.png`). El componente `ChatConversation` gestiona el prefijo `baseUrl` automáticamente.
- El blog está **desactivado** (`blog: false` en la configuración).
- No modificar los directorios `build/`, `node_modules/` ni `.docusaurus/` — son generados.
