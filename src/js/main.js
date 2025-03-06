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
      : '/ia-educacion/';
  
  // Set the raw content path for fetching markdown files
  const rawContentPath = isLocal
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
      
      // Handle the last message if there is one
      if (currentRole) {
        const processedContent = marked.parse(currentMessage.trim());
        chatHtml += processedContent + '\n</div>\n';
      }
      
      chatHtml += '</div>';
      return chatHtml;
    });
  }
  
  // Add a function to manually initialize the menu from the hard-coded list
  function initializeMenuAndContent() {
    const contentWrapper = document.getElementById('content-wrapper');
    const sidebar = document.querySelector('.sidebar-menu');
    
    // Clear existing content (in case of refresh)
    contentWrapper.innerHTML = '';
    sidebar.innerHTML = '';
    
    // Helper function to convert section ID to display name
    function sectionIdToDisplayName(sectionId) {
      // Remove -section suffix and replace underscores with spaces
      const baseName = sectionId.replace('-section', '').replace(/_/g, ' ');
      // Capitalize first letter of each word
      return baseName.split(' ').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
      ).join(' ');
    }
    
    // Define the sections that should be in the menu
    const sections = [
      { id: 'historia-section', title: 'Historia y LLMs' },
      { id: 'herramientas-section', title: 'Herramientas' },
      { id: 'prompt-section', title: 'Prompts' },
      { id: 'ejemplos-section', title: 'Ejemplos de prompts' },
      { id: 'docente-section', title: 'Uso docente' },
      { id: 'programando-section', title: 'Programando' }
    ];
    
    // Create menu items and sections
    sections.forEach(section => {
      // Create a section element if it doesn't exist
      let sectionElement = document.getElementById(section.id);
      if (!sectionElement) {
        sectionElement = document.createElement('section');
        sectionElement.id = section.id;
        sectionElement.className = 'content-section';
        contentWrapper.appendChild(sectionElement);
      }
      
      // Create menu item
      const menuItem = document.createElement('li');
      const menuLink = document.createElement('a');
      menuLink.href = '#';
      menuLink.setAttribute('data-target', section.id);
      menuLink.textContent = section.title;
      
      // Add click event handler
      menuLink.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Update active class
        document.querySelectorAll('.sidebar-menu a').forEach(item => item.classList.remove('active'));
        this.classList.add('active');
        
        // Show corresponding section with smooth transition
        document.querySelectorAll('.content-section').forEach(sect => {
          if (sect.id === section.id) {
            sect.classList.add('active');
            // Scroll to top of content with smooth animation
            contentWrapper.scrollTo({
              top: 0,
              behavior: 'smooth'
            });
          } else {
            sect.classList.remove('active');
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
    });
    
    // Activate the first section by default
    if (sidebar.firstElementChild && sidebar.firstElementChild.firstElementChild) {
      sidebar.firstElementChild.firstElementChild.click();
    }
  }
  
  // Function to handle GitHub Pages specific setup
  function setupForGitHubPages() {
    // Initialize the menu structure first
    initializeMenuAndContent();
    
    // Now load content for each section
    const files = [
      { file: '1_historia_y_llms.md', section: 'historia-section' },
      { file: '2_herramientas.md', section: 'herramientas-section' },
      { file: '3_prompt.md', section: 'prompt-section' },
      { file: '3b_ejemplos_prompts.md', section: 'ejemplos-section' },
      { file: '4_uso_docente.md', section: 'docente-section' },
      { file: '5_programando.md', section: 'programando-section' }
    ];
    
    let loadedCount = 0;
    
    // Load content for each section
    files.forEach(fileInfo => {
      const filePath = 'content/' + fileInfo.file;
      
      // Load the markdown file
      fetch((isLocal ? basePath : rawContentPath) + filePath)
        .then(response => {
          if (!response.ok) throw new Error('File not found: ' + filePath);
          return response.text();
        })
        .then(md => {
          // Process chat conversation syntax
          md = processChatSyntax(md);
          
          // Process images/links for each file
          if (!isLocal) {
            // For GitHub Pages: use raw content URL for images
            md = md.replace(/!\[(.*?)\]\((?!http)(.*?)\)/g, `![$1](${rawContentPath}$2)`);
            // Also handle HTML img tags with relative paths
            md = md.replace(/<img src=["']\.\/img\/(.*?)["']/g, function(match, imgPath) {
              return `<img src="${rawContentPath}content/img/${imgPath}"`;
            });
          } else {
            // Fix image paths for local development
            md = md.replace(/!\[(.*?)\]\(\.\/img\/(.*?)\)/g, `![$1](content/img/$2)`);
            // Also handle HTML img tags with relative paths
            md = md.replace(/<img src=["']\.\/(img\/.*?)["']/g, `<img src="content/$1"`);
          }
          
          // Render markdown and insert into the section
          const html = marked.parse(md);
          document.getElementById(fileInfo.section).innerHTML = html;
          
          // Track loading progress
          loadedCount++;
          
          // Add loaded class to body for CSS transitions when all content is loaded
          if (loadedCount === files.length) {
            document.body.classList.add('content-loaded');
          }
        })
        .catch(error => {
          console.error(`Error loading ${filePath}:`, error);
          document.getElementById(fileInfo.section).innerHTML = 
            `<div class="error">Error cargando ${filePath}: ${error.message}</div>`;
        });
    });
  }
  
  // Function to update the last commit date
  function updateCommitDate() {
    const dateElement = document.getElementById('lastCommitDate');
    if (!dateElement) return;
    
    if (!isLocal) {
      // For GitHub Pages, fetch the last commit date from GitHub API
      fetch('https://api.github.com/repos/avidaldo/ia-educacion/commits?per_page=1')
        .then(response => response.json())
        .then(data => {
          if (data && data.length > 0 && data[0].commit) {
            const commitDate = new Date(data[0].commit.author.date);
            dateElement.textContent = commitDate.toLocaleDateString();
          } else {
            dateElement.textContent = 'Fecha no disponible';
          }
        })
        .catch(error => {
          console.error('Error fetching last commit date:', error);
          dateElement.textContent = 'Fecha no disponible';
        });
    } else {
      // For local development, use current date
      dateElement.textContent = new Date().toLocaleDateString();
    }
  }
  
  // Initialize
  document.addEventListener('DOMContentLoaded', function() {
    // Update the commit date
    updateCommitDate();
    
    // Setup the site based on whether we're in local development or GitHub Pages
    setupForGitHubPages();
  });
  
  // On smaller screens, start with sidebar hidden
  if (window.innerWidth <= 768) {
    sidebar.classList.add('sidebar-hidden');
    contentWrapper.classList.add('full-width');
  }
}); 