// This script fetches the last commit date from GitHub API and updates the lastUpdateDate element
document.addEventListener('DOMContentLoaded', async function() {
  try {
    const owner = 'avidaldo';
    const repo = 'ia-edu2';
    const response = await fetch(`https://api.github.com/repos/${owner}/${repo}/commits?per_page=1`);
    
    if (!response.ok) {
      throw new Error('Failed to fetch from GitHub API');
    }
    
    const data = await response.json();
    if (data && data.length > 0) {
      const lastCommitDate = new Date(data[0].commit.author.date);
      const formattedDate = lastCommitDate.toLocaleDateString('es-ES', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
      });
      
      const lastUpdateElement = document.getElementById('lastUpdateDate');
      if (lastUpdateElement) {
        lastUpdateElement.textContent = formattedDate;
      }
    }
  } catch (error) {
    console.error('Error fetching last update date:', error);
    const lastUpdateElement = document.getElementById('lastUpdateDate');
    if (lastUpdateElement) {
      lastUpdateElement.textContent = 'No disponible';
    }
  }
}); 