// Enhanced interactivity for details/summary elements

document.addEventListener('DOMContentLoaded', function() {
  
  // Track details state in localStorage
  function saveDetailsState() {
    const detailsStates = {};
    const allDetails = document.querySelectorAll('details[id]');
    
    allDetails.forEach(details => {
      detailsStates[details.id] = details.open;
    });
    
    localStorage.setItem('detailsStates', JSON.stringify(detailsStates));
  }
  
  // Restore details state from localStorage
  function restoreDetailsState() {
    const saved = localStorage.getItem('detailsStates');
    if (saved) {
      const detailsStates = JSON.parse(saved);
      
      Object.keys(detailsStates).forEach(id => {
        const details = document.getElementById(id);
        if (details && detailsStates[id]) {
          details.open = true;
        }
      });
    }
  }
  
  // Add IDs to details elements if missing
  function addDetailsIds() {
    const allDetails = document.querySelectorAll('details');
    allDetails.forEach((details, index) => {
      if (!details.id) {
        const chapter = document.querySelector('h1')?.id || 'unknown';
        details.id = `details-${chapter}-${index}`;
      }
    });
  }
  
  // Enhance details elements
  function enhanceDetails() {
    const allDetails = document.querySelectorAll('details');
    
    allDetails.forEach(details => {
      // Save state on toggle
      details.addEventListener('toggle', saveDetailsState);
      
      // Add keyboard shortcuts
      const summary = details.querySelector('summary');
      if (summary) {
        summary.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            details.open = !details.open;
          }
        });
      }
      
      // Add animation class
      details.addEventListener('toggle', () => {
        if (details.open) {
          details.classList.add('details-opening');
          setTimeout(() => details.classList.remove('details-opening'), 300);
        }
      });
    });
  }
  
  // Create "Expand All" / "Collapse All" buttons for exercise sets
  function addExpandCollapseButtons() {
    const exerciseSets = document.querySelectorAll('.exercise-set');
    
    exerciseSets.forEach(set => {
      const details = set.querySelectorAll('details');
      if (details.length > 2) {
        const controls = document.createElement('div');
        controls.className = 'details-controls';
        controls.innerHTML = `
          <button class="btn-expand-all">Expand All</button>
          <button class="btn-collapse-all">Collapse All</button>
        `;
        
        set.insertBefore(controls, set.firstChild);
        
        controls.querySelector('.btn-expand-all').addEventListener('click', () => {
          details.forEach(d => d.open = true);
        });
        
        controls.querySelector('.btn-collapse-all').addEventListener('click', () => {
          details.forEach(d => d.open = false);
        });
      }
    });
  }
  
  // Progress tracking for exercises
  function trackExerciseCompletion() {
    const solutionDetails = document.querySelectorAll('details.exercise-solution');
    
    solutionDetails.forEach(details => {
      details.addEventListener('toggle', () => {
        if (details.open) {
          // Mark exercise as viewed
          const exercise = details.closest('.exercise-container');
          if (exercise) {
            exercise.classList.add('exercise-viewed');
            
            // Save to localStorage
            const exerciseId = exercise.id || exercise.querySelector('.exercise-title')?.textContent;
            if (exerciseId) {
              const viewed = JSON.parse(localStorage.getItem('viewedExercises') || '{}');
              const chapter = document.querySelector('h1')?.id || 'unknown';
              if (!viewed[chapter]) viewed[chapter] = [];
              if (!viewed[chapter].includes(exerciseId)) {
                viewed[chapter].push(exerciseId);
                localStorage.setItem('viewedExercises', JSON.stringify(viewed));
              }
            }
          }
        }
      });
    });
  }
  
  // Show completion stats
  function showCompletionStats() {
    const viewed = JSON.parse(localStorage.getItem('viewedExercises') || '{}');
    const currentChapter = document.querySelector('h1')?.id;
    
    if (currentChapter && viewed[currentChapter]) {
      const totalExercises = document.querySelectorAll('.exercise-container').length;
      const viewedCount = viewed[currentChapter].length;
      
      if (totalExercises > 0) {
        const stats = document.createElement('div');
        stats.className = 'exercise-stats';
        stats.innerHTML = `
          <div class="stats-content">
            <span class="stats-label">Exercises Completed:</span>
            <span class="stats-value">${viewedCount} / ${totalExercises}</span>
            <div class="stats-bar">
              <div class="stats-progress" style="width: ${(viewedCount/totalExercises)*100}%"></div>
            </div>
          </div>
        `;
        
        const firstExerciseSet = document.querySelector('.exercise-set');
        if (firstExerciseSet) {
          firstExerciseSet.insertBefore(stats, firstExerciseSet.firstChild);
        }
      }
    }
  }
  
  // Smart hint system
  function setupSmartHints() {
    const hintDetails = document.querySelectorAll('details.exercise-hint');
    
    hintDetails.forEach((hint, index) => {
      const exercise = hint.closest('.exercise-container');
      if (exercise) {
        // Track hint usage
        hint.addEventListener('toggle', () => {
          if (hint.open) {
            const hintsUsed = exercise.querySelectorAll('details.exercise-hint[open]').length;
            exercise.setAttribute('data-hints-used', hintsUsed);
            
            // Show encouragement based on hint usage
            if (hintsUsed === 1) {
              showMessage(exercise, "Good strategy! Starting with hints helps learning.", 'info');
            } else if (hintsUsed > 2) {
              showMessage(exercise, "Consider trying the problem before opening more hints.", 'warning');
            }
          }
        });
      }
    });
  }
  
  // Show temporary messages
  function showMessage(container, text, type = 'info') {
    const message = document.createElement('div');
    message.className = `exercise-message message-${type}`;
    message.textContent = text;
    container.appendChild(message);
    
    setTimeout(() => {
      message.classList.add('fade-out');
      setTimeout(() => message.remove(), 300);
    }, 3000);
  }
  
  // Initialize all features
  addDetailsIds();
  restoreDetailsState();
  enhanceDetails();
  addExpandCollapseButtons();
  trackExerciseCompletion();
  showCompletionStats();
  setupSmartHints();
  
  // Re-initialize when content changes
  const observer = new MutationObserver(() => {
    enhanceDetails();
  });
  
  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
});

// Additional styles for interactive features
const style = document.createElement('style');
style.textContent = `
  .details-controls {
    margin-bottom: 1rem;
    text-align: right;
  }
  
  .details-controls button {
    padding: 0.25rem 0.75rem;
    margin-left: 0.5rem;
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.875rem;
  }
  
  .details-controls button:hover {
    background-color: #5a6268;
  }
  
  .exercise-viewed {
    position: relative;
  }
  
  .exercise-viewed::after {
    content: "✓ Viewed";
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
    color: #28a745;
    font-weight: bold;
    font-size: 0.875rem;
  }
  
  .exercise-stats {
    background-color: #e7f3ff;
    border: 1px solid #2196f3;
    border-radius: 6px;
    padding: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .stats-content {
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  
  .stats-label {
    font-weight: bold;
    color: #0c5460;
  }
  
  .stats-value {
    font-size: 1.25rem;
    color: #2196f3;
    font-weight: bold;
  }
  
  .stats-bar {
    flex: 1;
    height: 20px;
    background-color: #cce5ff;
    border-radius: 10px;
    overflow: hidden;
  }
  
  .stats-progress {
    height: 100%;
    background-color: #2196f3;
    transition: width 0.3s ease;
  }
  
  .exercise-message {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    font-size: 0.875rem;
    z-index: 100;
    animation: slideIn 0.3s ease;
  }
  
  .message-info {
    background-color: #cce5ff;
    color: #004085;
    border: 1px solid #b8daff;
  }
  
  .message-warning {
    background-color: #fff3cd;
    color: #856404;
    border: 1px solid #ffeaa7;
  }
  
  .fade-out {
    animation: fadeOut 0.3s ease;
    opacity: 0;
  }
  
  @keyframes slideIn {
    from {
      opacity: 0;
      transform: translateX(-50%) translateY(-20px);
    }
    to {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }
  }
  
  @keyframes fadeOut {
    to {
      opacity: 0;
      transform: translateX(-50%) translateY(-10px);
    }
  }
  
  .details-opening .details-content {
    animation: detailsExpand 0.3s ease;
  }
  
  @keyframes detailsExpand {
    from {
      opacity: 0;
      max-height: 0;
    }
    to {
      opacity: 1;
      max-height: 1000px;
    }
  }
`;
document.head.appendChild(style);