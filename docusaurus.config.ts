import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Docencia con IA',
  tagline: 'Usando IAs para la docencia',
  favicon: 'img/favicon.ico',

  url: 'https://avidaldo.github.io',
  baseUrl: '/ia-educacion/',

  organizationName: 'avidaldo',
  projectName: 'ia-educacion',
  deploymentBranch: 'gh-pages',
  trailingSlash: true,

  onBrokenLinks: 'warn',
  markdown: {
    format: 'detect',
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },


  i18n: {
    defaultLocale: 'es',
    locales: ['es', 'gl'],
    localeConfigs: {
      es: {
        htmlLang: 'es-ES',
        label: 'Español',
      },
      gl: {
        htmlLang: 'gl',
        label: 'Galego',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        indexDocs: true,
        indexPages: true,
        language: ['es'],
      },
    ],
    require.resolve('./plugins/chat-data-plugin'),
  ],

  themeConfig: {
    // Replace with your project's social card
    // image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Docencia con IA',
      logo: {
        alt: 'Docencia con IA',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Contenidos',
        },
        {
          to: '/presentation',
          position: 'left',
          label: 'Presentación',
        },
        {
          type: 'localeDropdown',
          position: 'right',
        },
        {
          type: 'html',
          position: 'right',
          value: `\u003cdiv style=\"display: flex; flex-direction: column; align-items: flex-end; line-height: 1.2;\"\u003e
                  \u003cdiv style=\"font-size: 0.8rem; opacity: 0.8;\"\u003eÚltima actualización: 
                  ${new Date().toLocaleDateString('es-ES', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric'
          })}\u003c/div\u003e
                \u003c/div\u003e`,
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,

  scripts: [],
  staticDirectories: ['public', 'static'],
};

export default config;
