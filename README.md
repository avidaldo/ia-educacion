# Docencia con IA

Educational website built with Docusaurus to showcase AI tools and techniques for teaching.

**Live Site:** https://avidaldo.github.io/ia-educacion/

## 📋 Project Overview

This project is a Docusaurus-based static website that provides educational content about using AI in teaching. It features:

- 📚 Comprehensive documentation on AI tools for education
- 💬 Interactive chat conversation displays (loaded from YAML files)
- 🔍 Local search functionality (Spanish language support)
- 🌐 GitHub Pages deployment

## 🏗️ Architecture

The project follows Docusaurus's Static Site Generation (SSG) architecture with custom enhancements:

### Core Technologies

- **[Docusaurus](https://docusaurus.io/) v3.9.2**: Modern static website generator for documentation
- **React 18**: UI component framework
- **TypeScript**: Type-safe configuration and components
- **MDX**: Markdown with JSX component support

### Directory Structure

```
ia-educacion/
├── docs/                    # Documentation markdown/MDX files
├── src/
│   ├── components/          # React components
│   │   └── ChatConversation/  # Chat display component
│   ├── css/                 # Custom styles
│   └── pages/               # Custom pages
├── static/
│   └── data/
│       └── chats/           # YAML chat conversation files
├── plugins/
│   └── chat-data-plugin.js  # Custom Docusaurus plugin
├── .github/
│   └── workflows/           # GitHub Actions CI/CD
├── docusaurus.config.ts     # Docusaurus configuration
└── sidebars.ts              # Documentation sidebar structure
```

### Key Components

#### 1. Static Site Generation (SSG)
All content is generated at build time, ensuring:
- Fast page loads
- No client-side data fetching
- Better SEO
- No runtime network requests

#### 2. Documentation Pages
Markdown/MDX files in the `docs/` directory are automatically converted to web pages with navigation, search, and responsive design.

#### 3. Chat Conversation Component
A custom React component (`ChatConversation`) that displays AI chat conversations with:
- Markdown support (including code blocks, tables, and GFM)
- User/Assistant message styling
- Theme-aware design (light/dark mode)

## 🔌 Custom Chat Data Plugin

The project includes a custom Docusaurus plugin (`chat-data-plugin.js`) that implements build-time data loading:

### How It Works

1. **Build-Time Loading**: During `npm run build`, the plugin:
   - Scans `static/data/chats/` for YAML files
   - Parses each YAML file containing chat conversations
   - Makes the data available globally to all components

2. **Data Format**: Chat YAML files follow this structure:
   ```yaml
   messages:
     - role: user
       content: Your question here
     - role: assistant
       content: |
         AI response with markdown support.
         Can include **bold**, *italic*, code, etc.
   ```

3. **Usage in MDX**:
   ```mdx
   import { ChatConversation } from '@site/src/components/ChatConversation';

   <ChatConversation source="/data/chats/example-chat.yaml" />
   ```

### Benefits

- ✅ **Build-time validation**: YAML parsing errors fail the build, not at runtime
- ✅ **Better performance**: No network requests or client-side fetching
- ✅ **SSG-compliant**: Follows Docusaurus best practices
- ✅ **Type safety**: Full TypeScript support

## 🚀 Local Development

### Prerequisites

- **Node.js**: v20.0 or higher
- **npm**: Comes with Node.js

### Setup and Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/avidaldo/ia-educacion.git
   cd ia-educacion
   ```

2. **Install dependencies**:
   ```bash
   npm ci
   ```

3. **Start development server**:
   ```bash
   npm run start
   ```

   The site will open at `http://localhost:3000/ia-educacion/`

4. **Build for production** (optional):
   ```bash
   npm run build
   ```

   Output will be in the `build/` directory.

5. **Serve production build** (optional):
   ```bash
   npm run serve
   ```

### Available Scripts

| Script | Description |
|--------|-------------|
| `npm start` | Start development server with hot reload |
| `npm run build` | Build production-ready static site |
| `npm run serve` | Serve the production build locally |
| `npm run clear` | Clear Docusaurus cache |
| `npm run typecheck` | Run TypeScript type checking |

## 🌐 GitHub Pages Deployment

The site is automatically deployed to GitHub Pages using GitHub Actions.

### Deployment Workflow

1. **Trigger**: Push to `master` branch
2. **Build Process** (`.github/workflows/deploy.yml`):
   - Checkout code
   - Setup Node.js v20
   - Install dependencies with `npm ci`
   - Build site with `npm run build`
   - Deploy `build/` directory to `gh-pages` branch

3. **Hosting**: GitHub Pages serves the `gh-pages` branch at:
   - **URL**: https://avidaldo.github.io/ia-educacion/

### Configuration

Key deployment settings in `docusaurus.config.ts`:

```typescript
{
  url: 'https://avidaldo.github.io',
  baseUrl: '/ia-educacion/',
  organizationName: 'avidaldo',
  projectName: 'ia-educacion',
  deploymentBranch: 'gh-pages',
  trailingSlash: false
}
```

### Manual Deployment

To manually deploy (requires GitHub permissions):

```bash
npm run deploy
```

## 🎨 Features

- **🌍 Internationalization**: Configured for Spanish (es-ES)
- **🔍 Search**: Local search with `@easyops-cn/docusaurus-search-local`
- **🎨 Theming**: Light/dark mode with Prism syntax highlighting
- **📱 Responsive**: Mobile-friendly design
- **♿ Accessible**: Follows web accessibility standards

## 📝 Adding Content

### Add a New Documentation Page

1. Create a new `.md` or `.mdx` file in `docs/`
2. Add frontmatter:
   ```markdown
   ---
   sidebar_position: 1
   title: My Page Title
   ---
   
   # Content here
   ```

### Add a New Chat Conversation

1. Create a YAML file in `static/data/chats/`:
   ```yaml
   model: "GPT-4"  # Optional
   date: "2024-12-21"  # Optional
   messages:
     - role: user
       content: Question?
     - role: assistant
       content: Answer!
   ```

2. Reference it in your MDX:
   ```mdx
   import { ChatConversation } from '@site/src/components/ChatConversation';

   <ChatConversation source="/data/chats/your-chat.yaml" />
   ```

## 📄 License

This project is educational content for teaching purposes.

## 👤 Author

**avidaldo**
- GitHub: [@avidaldo](https://github.com/avidaldo)
- Website: https://avidaldo.github.io/ia-educacion/

---

Built with [Docusaurus](https://docusaurus.io/) 🦖
