import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Docencia con IA',
  tagline: 'Usando IAs para la docencia',
  favicon: 'img/favicon.ico',

  url: 'https://avidaldo.github.io',
  baseUrl: '/ia-edu2/',

  organizationName: 'avidaldo',
  projectName: 'ia-edu2',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',


  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
    localeConfigs: {
      es: {
        htmlLang: 'es-ES',
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
          type: 'html',
          position: 'right',
          value: `<div style="display: flex; flex-direction: column; align-items: flex-end; line-height: 1.2;">
                  <div style="font-size: 0.8rem; opacity: 0.8;">Última actualización: 
                  ${new Date().toLocaleDateString('es-ES', {
                    day: '2-digit',
                    month: '2-digit',
                    year: 'numeric'
                  })}</div>
                </div>`,
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
