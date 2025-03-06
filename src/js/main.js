document.addEventListener('DOMContentLoaded', function() {
  // Elements
  const menuToggle = document.getElementById('menu-toggle');
  const sidebar = document.getElementById('sidebar');
  const contentWrapper = document.getElementById('content-wrapper');
  
  // Check if we're in local development or GitHub Pages
  const isLocal = window.location.protocol === 'file:' || 
                 window.location.hostname === 'localhost' || 
                 window.location.hostname === '127.0.0.1';
  
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
  
  // Setup menu click handlers (for the predefined menu in HTML)
  function setupMenuHandlers() {
    const menuLinks = document.querySelectorAll('.sidebar-menu a');
    
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
    
    // Activate the first menu item by default
    if (menuLinks.length > 0) {
      menuLinks[0].click();
    }
  }
  
  // Load content for sections
  function loadContent() {
    // Define the mapping between section IDs and content files
    const contentMap = [
      { file: '1_historia_y_llms.md', section: 'historia-section' },
      { file: '2_herramientas.md', section: 'herramientas-section' },
      { file: '3_prompt.md', section: 'prompt-section' },
      { file: '3b_ejemplos_prompts.md', section: 'ejemplos-section' },
      { file: '4_uso_docente.md', section: 'docente-section' },
      { file: '5_programando.md', section: 'programando-section' }
    ];
    
    let loadedCount = 0;
    const totalFiles = contentMap.length;
    
    // Load content for each section
    contentMap.forEach(item => {
      const filePath = 'content/' + item.file;
      const sectionElement = document.getElementById(item.section);
      
      if (!sectionElement) {
        console.error(`Section element with ID "${item.section}" not found`);
        loadedCount++;
        return;
      }
      
      // Display loading indicator in the section
      sectionElement.innerHTML = '<div class="loading">Cargando contenido...</div>';
      
      // Determine URL for fetching content
      let fetchUrl = '';
      if (isLocal) {
        fetchUrl = filePath;
      } else {
        fetchUrl = rawContentPath + filePath;
      }
      
      // Log the URL for debugging
      console.log(`Fetching content from: ${fetchUrl}`);
      
      // Load the markdown file
      fetch(fetchUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error(`Failed to load ${filePath} (Status: ${response.status})`);
          }
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
          sectionElement.innerHTML = html;
          
          // Track loading progress
          loadedCount++;
          console.log(`Loaded ${loadedCount}/${totalFiles} files`);
          
          // Add loaded class to body for CSS transitions when all content is loaded
          if (loadedCount === totalFiles) {
            document.body.classList.add('content-loaded');
          }
        })
        .catch(error => {
          console.error(`Error loading ${filePath}:`, error);
          sectionElement.innerHTML = 
            `<div class="error">Error cargando ${filePath}: ${error.message}</div>`;
          
          // Still track loading even on error
          loadedCount++;
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
  
  // Initialize everything
  function initialize() {
    // Setup menu click handlers first
    setupMenuHandlers();
    
    // Load content for all sections
    loadContent();
    
    // Update the commit date
    updateCommitDate();
    
    // Add debug info to console
    console.log(`Running in ${isLocal ? 'local' : 'GitHub Pages'} mode`);
    console.log(`Base path: ${basePath}`);
    console.log(`Raw content path: ${rawContentPath}`);
  }
  
  // Start initialization
  initialize();
  
  // On smaller screens, start with sidebar hidden
  if (window.innerWidth <= 768) {
    sidebar.classList.add('sidebar-hidden');
    contentWrapper.classList.add('full-width');
  }
}); 