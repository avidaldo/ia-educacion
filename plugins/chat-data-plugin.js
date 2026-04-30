const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { glob } = require('glob');

/**
 * Loads all YAML chat files from a directory and returns them keyed by
 * their source path (e.g. "/data/chats/specific-role.yaml").
 */
async function loadYamlChats(dir) {
  const chats = {};
  if (!fs.existsSync(dir)) {
    return chats;
  }

  const files = await glob('**/*.{yaml,yml}', { cwd: dir });

  for (const file of files) {
    try {
      const fullPath = path.join(dir, file);
      const content = fs.readFileSync(fullPath, 'utf8');
      const data = yaml.load(content);
      const key = `/data/chats/${file}`;
      chats[key] = data;
    } catch (error) {
      // Fail build if YAML is invalid - better than runtime errors
      throw new Error(`Failed to load chat ${file}: ${error.message}`);
    }
  }

  return chats;
}

/**
 * Docusaurus plugin to load chat conversation YAML files at build time.
 * This eliminates runtime fetch() calls and follows SSG best practices.
 *
 * Locale support:
 *   - Default chats are loaded from static/data/chats/
 *   - Per-locale overrides are loaded from i18n/{locale}/chat-data/
 *   - Translated files override the default ones; untranslated chats
 *     fall back to the default language automatically.
 */
module.exports = function chatDataPlugin(context, options) {
  return {
    name: 'docusaurus-plugin-chat-data',

    async loadContent() {
      const { i18n } = context;
      const locale = i18n.currentLocale;
      const defaultLocale = i18n.defaultLocale;

      // 1. Load default chats (static/data/chats/)
      const defaultDir = path.join(context.siteDir, 'static/data/chats');
      const chats = await loadYamlChats(defaultDir);

      const defaultCount = Object.keys(chats).length;
      console.log(`Loaded ${defaultCount} default chat conversations`);

      // 2. Override with locale-specific chats if not the default locale
      if (locale !== defaultLocale) {
        const localizedDir = path.join(
          context.siteDir,
          'i18n',
          locale,
          'chat-data'
        );
        const localizedChats = await loadYamlChats(localizedDir);
        const overrideCount = Object.keys(localizedChats).length;

        if (overrideCount > 0) {
          Object.assign(chats, localizedChats);
          console.log(
            `Overrode ${overrideCount} chat(s) with ${locale} translations`
          );
        }
      }

      // Log final summary
      for (const key of Object.keys(chats)) {
        console.log(`✓ Chat ready: ${key}`);
      }

      return chats;
    },

    /**
     * Make loaded chat data available globally to all components
     */
    async contentLoaded({ content, actions }) {
      const { setGlobalData } = actions;
      setGlobalData(content);
    },
  };
};
