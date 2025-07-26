// Interactive code features for Python Step by Step

document.addEventListener('DOMContentLoaded', function() {
  
  // Add copy button to all code blocks
  function addCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre.sourceCode');
    
    codeBlocks.forEach(block => {
      // Skip if button already exists
      if (block.querySelector('.copy-code-button')) return;
      
      const button = document.createElement('button');
      button.className = 'copy-code-button';
      button.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V2zm2 0v8h8V2H6zM2 6a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-2H8v2H2V8h2V6H2z"/></svg> Copy';
      button.title = 'Copy code to clipboard';
      
      button.addEventListener('click', async () => {
        const code = block.querySelector('code').textContent;
        try {
          await navigator.clipboard.writeText(code);
          button.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M12.736 3.336a.75.75 0 0 1 0 1.061l-6.5 6.5a.75.75 0 0 1-1.061 0l-3.5-3.5a.75.75 0 1 1 1.061-1.061l2.969 2.969 5.969-5.969a.75.75 0 0 1 1.061 0z"/></svg> Copied!';
          button.classList.add('copied');
          
          setTimeout(() => {
            button.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M4 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V2zm2 0v8h8V2H6zM2 6a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-2H8v2H2V8h2V6H2z"/></svg> Copy';
            button.classList.remove('copied');
          }, 2000);
        } catch (err) {
          console.error('Failed to copy:', err);
          button.textContent = 'Failed to copy';
        }
      });
      
      block.style.position = 'relative';
      block.appendChild(button);
    });
  }
  
  // Add line highlighting on hover
  function addLineHighlighting() {
    const codeLines = document.querySelectorAll('.sourceCode code > span');
    
    codeLines.forEach(line => {
      line.addEventListener('mouseenter', function() {
        this.classList.add('hover-highlight');
      });
      
      line.addEventListener('mouseleave', function() {
        this.classList.remove('hover-highlight');
      });
    });
  }
  
  // Create output visualization for code blocks
  function addOutputVisualization() {
    const codeOutputPairs = document.querySelectorAll('.code-with-output');
    
    codeOutputPairs.forEach(pair => {
      const runButton = document.createElement('button');
      runButton.className = 'run-code-button';
      runButton.innerHTML = '▶ Show Output';
      runButton.title = 'Show/hide code output';
      
      const output = pair.querySelector('.code-output');
      if (output) {
        output.style.display = 'none';
        
        runButton.addEventListener('click', () => {
          if (output.style.display === 'none') {
            output.style.display = 'block';
            runButton.innerHTML = '▼ Hide Output';
            output.classList.add('output-animate-in');
          } else {
            output.style.display = 'none';
            runButton.innerHTML = '▶ Show Output';
          }
        });
        
        pair.querySelector('.sourceCode').appendChild(runButton);
      }
    });
  }
  
  // Add step-through functionality for traced code
  function addStepThrough() {
    const tracedBlocks = document.querySelectorAll('.traced-code');
    
    tracedBlocks.forEach(block => {
      const lines = block.querySelectorAll('code > span');
      let currentLine = 0;
      
      const controls = document.createElement('div');
      controls.className = 'step-controls';
      controls.innerHTML = `
        <button class="step-button step-reset" title="Reset">⟲</button>
        <button class="step-button step-prev" title="Previous step">←</button>
        <span class="step-indicator">Step <span class="current-step">0</span> of ${lines.length}</span>
        <button class="step-button step-next" title="Next step">→</button>
        <button class="step-button step-play" title="Play all">▶</button>
      `;
      
      block.appendChild(controls);
      
      function updateHighlight() {
        lines.forEach((line, index) => {
          line.classList.toggle('current-line', index === currentLine);
          line.classList.toggle('executed-line', index < currentLine);
        });
        controls.querySelector('.current-step').textContent = currentLine;
      }
      
      controls.querySelector('.step-next').addEventListener('click', () => {
        if (currentLine < lines.length) {
          currentLine++;
          updateHighlight();
        }
      });
      
      controls.querySelector('.step-prev').addEventListener('click', () => {
        if (currentLine > 0) {
          currentLine--;
          updateHighlight();
        }
      });
      
      controls.querySelector('.step-reset').addEventListener('click', () => {
        currentLine = 0;
        updateHighlight();
      });
      
      controls.querySelector('.step-play').addEventListener('click', async () => {
        for (let i = currentLine; i <= lines.length; i++) {
          currentLine = i;
          updateHighlight();
          await new Promise(resolve => setTimeout(resolve, 500));
        }
      });
      
      updateHighlight();
    });
  }
  
  // Add annotation tooltips
  function addAnnotationTooltips() {
    const annotations = document.querySelectorAll('.code-annotation');
    
    annotations.forEach(annotation => {
      const tooltip = document.createElement('div');
      tooltip.className = 'annotation-tooltip';
      tooltip.textContent = annotation.getAttribute('data-annotation');
      tooltip.style.display = 'none';
      
      annotation.appendChild(tooltip);
      
      annotation.addEventListener('mouseenter', () => {
        tooltip.style.display = 'block';
      });
      
      annotation.addEventListener('mouseleave', () => {
        tooltip.style.display = 'none';
      });
    });
  }
  
  // Initialize all features
  addCopyButtons();
  addLineHighlighting();
  addOutputVisualization();
  addStepThrough();
  addAnnotationTooltips();
  
  // Re-initialize when new content is loaded (for dynamic content)
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.addedNodes.length) {
        addCopyButtons();
        addLineHighlighting();
        addOutputVisualization();
        addStepThrough();
        addAnnotationTooltips();
      }
    });
  });
  
  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
});

// CSS for interactive features
const style = document.createElement('style');
style.textContent = `
  .copy-code-button {
    position: absolute;
    top: 8px;
    right: 8px;
    padding: 4px 8px;
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    opacity: 0;
    transition: opacity 0.2s, background-color 0.2s;
  }
  
  .sourceCode:hover .copy-code-button {
    opacity: 1;
  }
  
  .copy-code-button:hover {
    background-color: #5a6268;
  }
  
  .copy-code-button.copied {
    background-color: #28a745;
  }
  
  .hover-highlight {
    background-color: rgba(255, 235, 59, 0.2);
    display: block;
    margin: 0 -1em;
    padding: 0 1em;
  }
  
  .run-code-button {
    position: absolute;
    bottom: 8px;
    right: 8px;
    padding: 4px 12px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
    font-weight: bold;
  }
  
  .run-code-button:hover {
    background-color: #218838;
  }
  
  .output-animate-in {
    animation: slideDown 0.3s ease-out;
  }
  
  @keyframes slideDown {
    from {
      opacity: 0;
      transform: translateY(-10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .step-controls {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px;
    background-color: #f8f9fa;
    border-top: 1px solid #dee2e6;
    border-radius: 0 0 6px 6px;
  }
  
  .step-button {
    padding: 4px 8px;
    background-color: #6c757d;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
  }
  
  .step-button:hover {
    background-color: #5a6268;
  }
  
  .step-indicator {
    font-size: 12px;
    color: #6c757d;
  }
  
  .current-line {
    background-color: rgba(33, 150, 243, 0.3);
    display: block;
    margin: 0 -1em;
    padding: 0 1em;
    border-left: 3px solid #2196f3;
  }
  
  .executed-line {
    opacity: 0.6;
  }
  
  .annotation-tooltip {
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    background-color: #333;
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    white-space: nowrap;
    z-index: 1000;
    margin-bottom: 4px;
  }
  
  .annotation-tooltip::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    border-width: 4px;
    border-style: solid;
    border-color: #333 transparent transparent transparent;
  }
`;
document.head.appendChild(style);