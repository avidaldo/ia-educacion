const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { glob } = require('glob');

/**
 * Docusaurus plugin to load chat conversation YAML files at build time
 * This eliminates runtime fetch() calls and follows SSG best practices
 */
module.exports = function chatDataPlugin(context, options) {
  return {
    name: 'docusaurus-plugin-chat-data',
    
    /**
     * Load all YAML chat files from static/data/chats directory
     * This runs during the build process
     */
    async loadContent() {
      const chatDir = path.join(context.siteDir, 'static/data/chats');
      
      // Check if directory exists
      if (!fs.existsSync(chatDir)) {
        console.warn(`Chat data directory not found: ${chatDir}`);
        return {};
      }
      
      // Find all YAML files
      const files = await glob('**/*.{yaml,yml}', { cwd: chatDir });
      
      const chats = {};
      for (const file of files) {
        try {
          const fullPath = path.join(chatDir, file);
          const content = fs.readFileSync(fullPath, 'utf8');
          const data = yaml.load(content);
          
          // Use path as key (matching the source prop format)
          const key = `/data/chats/${file}`;
          chats[key] = data;
          
          console.log(`✓ Loaded chat: ${key}`);
        } catch (error) {
          // Fail build if YAML is invalid - better than runtime errors
          throw new Error(`Failed to load chat ${file}: ${error.message}`);
        }
      }
      
      console.log(`Loaded ${Object.keys(chats).length} chat conversations`);
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
