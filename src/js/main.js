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
    // Get the content container
    const contentWrapper = document.getElementById('content-wrapper');
    const sidebar = document.querySelector('.sidebar-menu');
    
    // Clear existing content (in case of refresh)
    contentWrapper.innerHTML = '';
    sidebar.innerHTML = '';
    
    // Helper function to convert filename to section ID
    function fileNameToSectionId(fileName) {
      // Remove numbers and file extension, convert to lowercase
      return fileName.replace(/^\d+_/, '').replace(/\.md$/, '').replace(/-/g, '_') + '-section';
    }
    
    // Fetch the list of markdown files from the content directory
    fetch(basePath + 'content/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to access content directory');
        }
        // For local development or GitHub Pages, we need to handle this differently
        if (isLocal) {
          // For local development, we'll use a fixed list of files from the directory
          return listContentFiles();
        } else {
          // For GitHub Pages or deployed sites, parse the directory listing
          return response.text().then(html => {
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const links = Array.from(doc.querySelectorAll('a'));
            
            // Filter for markdown files only
            return links
              .map(link => link.getAttribute('href'))
              .filter(href => href && href.endsWith('.md'))
              .map(href => href);
          });
        }
      })
      .then(files => {
        // Sort files by filename (which might include numeric prefixes for order)
        files.sort();
        
        // Track loading progress
        let loadedCount = 0;
        
        // Process each markdown file
        files.forEach(file => {
          // For GitHub, file is just the filename; for local we need to ensure it's a relative path
          const fileName = file.split('/').pop();
          const filePath = 'content/' + fileName;
          
          // Create a section ID based on the filename
          const sectionId = fileNameToSectionId(fileName);
          
          // Create a new section element
          const sectionElement = document.createElement('section');
          sectionElement.id = sectionId;
          sectionElement.className = 'content-section';
          contentWrapper.appendChild(sectionElement);
          
          // Load the markdown file
          fetch(basePath + filePath)
            .then(response => {
              if (!response.ok) throw new Error('File not found: ' + filePath);
              return response.text();
            })
            .then(md => {
              // Process chat conversation syntax
              md = processChatSyntax(md);
              
              // Process images/links for each file
              if (!isLocal) {
                md = md.replace(/!\[(.*?)\]\((?!http)(.*?)\)/g, `![$1](${basePath}$2)`);
                // Also handle HTML img tags with relative paths
                md = md.replace(/<img src=["']\.\/img\/(.*?)["']/g, function(match, imgPath) {
                  return `<img src="${basePath}content/img/${imgPath}"`;
                });
              } else {
                // Fix image paths for local development
                md = md.replace(/!\[(.*?)\]\(\.\/img\/(.*?)\)/g, `![$1](content/img/$2)`);
                // Also handle HTML img tags with relative paths
                md = md.replace(/<img src=["']\.\/(img\/.*?)["']/g, `<img src="content/$1"`);
              }
              
              // Render markdown and insert into the section
              const html = marked.parse(md);
              sectionElement.innerHTML = html;
              
              // Extract title (main heading) from the markdown
              const titleMatch = md.match(/^# (.*?)$/m);
              const menuTitle = titleMatch && titleMatch[1] ? titleMatch[1] : fileName.replace(/^\d+_/, '').replace(/\.md$/, '');
              
              // Create menu item
              const menuItem = document.createElement('li');
              const menuLink = document.createElement('a');
              menuLink.href = '#';
              menuLink.setAttribute('data-target', sectionId);
              menuLink.textContent = menuTitle;
              
              // Add click event handler
              menuLink.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Update active class
                document.querySelectorAll('.sidebar-menu a').forEach(item => item.classList.remove('active'));
                this.classList.add('active');
                
                // Show corresponding section with smooth transition
                document.querySelectorAll('.content-section').forEach(section => {
                  if (section.id === sectionId) {
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
                  document.getElementById('sidebar').classList.add('sidebar-hidden');
                  contentWrapper.classList.add('full-width');
                }
              });
              
              menuItem.appendChild(menuLink);
              sidebar.appendChild(menuItem);
              
              // Track loading progress
              loadedCount++;
              
              // All content loaded, initialize content display
              if (loadedCount === files.length) {
                // Add a small delay to ensure proper render
                setTimeout(() => {
                  // Activate the first section by default
                  if (sidebar.firstElementChild && sidebar.firstElementChild.firstElementChild) {
                    sidebar.firstElementChild.firstElementChild.click();
                  }
                  
                  // Add loaded class to body for CSS transitions
                  document.body.classList.add('content-loaded');
                }, 100);
              }
            })
            .catch(error => {
              console.error(`Error loading ${filePath}:`, error);
              document.getElementById(sectionId).innerHTML = 
                `<div class="error">Error cargando ${filePath}: ${error.message}</div>`;
                
              // Still track loading even on error
              loadedCount++;
            });
        });
      })
      .catch(error => {
        contentWrapper.innerHTML = `<div class="error">Error loading content directory: ${error.message}</div>`;
        console.error('Error loading content directory:', error);
      });
  }
  
  // For local development, fall back to a fixed list of files
  function listContentFiles() {
    return [
      '1_historia_y_llms.md',
      '2_herramientas.md',
      '3_prompt.md',
      '3b_ejemplos_prompts.md',
      '4_uso_docente.md',
      '5_programando.md'
    ];
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