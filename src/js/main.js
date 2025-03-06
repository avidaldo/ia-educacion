document.addEventListener('DOMContentLoaded', function() {
  // Elements
  const menuToggle = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('sidebar');
  const contentWrapper = document.getElementById('content-wrapper');
  const menuLinks = document.querySelectorAll('.sidebar-menu a');
  
  // Check if we're in local development or GitHub Pages
  const isLocal = window.location.protocol === 'file:' || 
                 window.location.hostname === 'localhost' || 
                 window.location.hostname === '127.0.0.1';
  
  // Get the current directory path for local development
  function getLocalBasePath() {
    const pathSegments = window.location.pathname.split('/');
    // Remove the last segment (index.html) and empty segments
    const filteredSegments = pathSegments.filter(segment => segment && segment !== 'index.html');
    // Build the path with trailing slash
    return filteredSegments.length ? '/' + filteredSegments.join('/') + '/' : '/';
  }
  
  // Set the base path accordingly
  const basePath = isLocal 
      ? '' 
      : 'https://raw.githubusercontent.com/avidaldo/ia-educacion/master/';
  
  // Toggle sidebar
  menuToggle.addEventListener('click', function() {
    sidebar.classList.toggle('sidebar-hidden');
    contentWrapper.classList.toggle('full-width');
  });
  
  // Handle menu clicks
  menuLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Update active class
      menuLinks.forEach(item => item.classList.remove('active'));
      this.classList.add('active');
      
      // Show corresponding section with smooth transition
      const targetId = this.getAttribute('data-target');
      document.querySelectorAll('.content-section').forEach(section => {
        if (section.id === targetId) {
          section.classList.add('active');
          // Scroll to top of content with smooth animation
          contentWrapper.scrollTo({
            top: 0,
            behavior: 'smooth'
          });
        } else {
          section.classList.remove('active');
        }
      });
      
      // On mobile, hide sidebar after selection
      if (window.innerWidth <= 768) {
        sidebar.classList.add('sidebar-hidden');
        contentWrapper.classList.add('full-width');
      }
    });
  });
  
  // Load markdown content
  function loadMarkdownContent() {
    // Define markdown files to load
    const mdFiles = [
      { id: 'historia-section', file: 'content/1_historia_y_llms.md' },
      { id: 'herramientas-section', file: 'content/2_herramientas.md' },
      { id: 'prompt-section', file: 'content/3_prompt.md' },
      { id: 'zeroshot-section', file: 'content/3b_zero-shot.md' },
      { id: 'ejemplos-section', file: 'content/3b_ejemplos_prompts.md' },
      { id: 'docente-section', file: 'content/4_uso_docente.md' },
      { id: 'programando-section', file: 'content/5_programando.md' }
    ];
    
    // Track loading progress
    let loadedCount = 0;
    
    // Load each file
    mdFiles.forEach(item => {
      fetch(basePath + item.file)
        .then(response => {
          if (!response.ok) throw new Error('File not found: ' + item.file);
          return response.text();
        })
        .then(md => {
          // Process chat conversation syntax
          md = processChatSyntax(md);
          
          // Process images/links for each file - only for GitHub paths
          if (!isLocal) {
            md = md.replace(/!\[(.*?)\]\((?!http)(.*?)\)/g, `![$1](${basePath}$2)`);
          } else {
            // Fix image paths for local development
            md = md.replace(/!\[(.*?)\]\(\.\/img\/(.*?)\)/g, `![$1](content/img/$2)`);
          }
          
          // Render markdown and insert into corresponding section
          const html = marked.parse(md);
          document.getElementById(item.id).innerHTML = html;
          
          // Extract title from the markdown for the menu item
          const titleMatch = md.match(/^# (.*?)$/m);
          if (titleMatch && titleMatch[1]) {
            const menuItem = document.querySelector(`[data-target="${item.id}"]`);
            if (menuItem) {
              menuItem.textContent = titleMatch[1];
            }
          }
          
          // Track loading progress
          loadedCount++;
          
          // All content loaded, initialize content display
          if (loadedCount === mdFiles.length) {
            // Add a small delay to ensure proper render
            setTimeout(() => {
              // Activate the first section by default
              if (menuLinks.length > 0) {
                menuLinks[0].click();
              }
              
              // Add loaded class to body for CSS transitions
              document.body.classList.add('content-loaded');
            }, 100);
          }
        })
        .catch(error => {
          console.error(`Error loading ${item.file}:`, error);
          document.getElementById(item.id).innerHTML = 
            `<div class="error">Error cargando ${item.file}: ${error.message}</div>`;
            
          // Still track loading even on error
          loadedCount++;
        });
    });
  }
  
  // Function to process chat conversation syntax
  function processChatSyntax(markdown) {
    // Look for chat conversation blocks
    const chatRegex = /```chat\s+([\s\S]*?)```/g;
    
    return markdown.replace(chatRegex, function(match, chatContent) {
      let chatHtml = '<div class="chat-container">\n';
      
      // Split by lines and process each line
      const lines = chatContent.split('\n');
      let currentRole = null;
      let currentMessage = '';
      
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        
        if (line.startsWith('USER:')) {
          // If we were already in a message block, process it and close it
          if (currentRole) {
            // Process markdown in the current message
            const processedContent = marked.parse(currentMessage.trim());
            chatHtml += processedContent + '\n</div>\n';
          }
          
          // Start a new user message
          chatHtml += '<div class="user-message">\n';
          currentMessage = line.substring(5).trim() + '\n';
          currentRole = 'user';
        } 
        else if (line.startsWith('ASSISTANT:')) {
          // If we were already in a message block, process it and close it
          if (currentRole) {
            // Process markdown in the current message
            const processedContent = marked.parse(currentMessage.trim());
            chatHtml += processedContent + '\n</div>\n';
          }
          
          // Start a new assistant message
          chatHtml += '<div class="assistant-message">\n';
          currentMessage = line.substring(10).trim() + '\n';
          currentRole = 'assistant';
        }
        else if (currentRole && line.trim() !== '') {
          // Continue the current message
          currentMessage += line + '\n';
        }
      }
      
      // Process and close the last message if needed
      if (currentRole) {
        // Process markdown in the current message
        const processedContent = marked.parse(currentMessage.trim());
        chatHtml += processedContent + '\n</div>\n';
      }
      
      chatHtml += '</div>';
      return chatHtml;
    });
  }
  
  // Update commit date function
  function updateCommitDate() {
    fetch('https://api.github.com/repos/avidaldo/ia-educacion/commits?per_page=1')
      .then(response => response.json())
      .then(commits => {
        const commitDate = new Date(commits[0].commit.author.date);
        const dateElements = document.querySelectorAll('#lastCommitDate');
        dateElements.forEach(el => {
          el.textContent = commitDate.toLocaleDateString('es-ES', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
          });
        });
      })
      .catch(() => {
        const dateElements = document.querySelectorAll('#lastCommitDate');
        dateElements.forEach(el => {
          el.textContent = 'Fecha no disponible';
        });
      });
  }
  
  // Initialize the page
  loadMarkdownContent();
  updateCommitDate();
  
  // On smaller screens, start with sidebar hidden
  if (window.innerWidth <= 768) {
    sidebar.classList.add('sidebar-hidden');
    contentWrapper.classList.add('full-width');
  }
}); 