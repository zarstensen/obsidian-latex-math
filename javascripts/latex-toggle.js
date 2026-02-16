document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.arithmatex').forEach(function(block) {
    const source = block.querySelector('script, annotation')?.textContent || 
                   block.textContent.trim();
    
    const wrapper = document.createElement('div');
    wrapper.className = 'latex-toggle-wrapper';
    
    const button = document.createElement('button');
    button.className = 'latex-toggle-btn';
    button.textContent = 'Show Source';
    
    const sourceBlock = document.createElement('pre');
    sourceBlock.className = 'latex-source';
    sourceBlock.style.display = 'none';
    sourceBlock.textContent = source;
    
    block.parentNode.insertBefore(wrapper, block);
    wrapper.appendChild(button);
    wrapper.appendChild(block);
    wrapper.appendChild(sourceBlock);
    
    button.addEventListener('click', function() {
      const isSourceVisible = sourceBlock.style.display !== 'none';
      sourceBlock.style.display = isSourceVisible ? 'none' : 'block';
      block.style.display = isSourceVisible ? 'block' : 'none';
      button.textContent = isSourceVisible ? 'Show Source' : 'Show Rendered';
    });
  });
});