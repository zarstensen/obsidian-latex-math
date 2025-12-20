// Add custom button to header
document.addEventListener("DOMContentLoaded", function () {
  // Find the search button
  const searchButton = document.querySelector('[data-md-component="search"]');

  if (searchButton) {
    // Create custom button
    const customButton = document.createElement('button');
    customButton.className = 'md-header__button md-icon custom-header-button';
    customButton.setAttribute('title', 'Download Documentation');
    customButton.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
      <path d="M2 12H4V17H20V12H22V17C22 18.11 21.11 19 20 19H4C2.9 19 2 18.11 2 17V12M12 15L17.55 9.54L16.13 8.13L13 11.25V2H11V11.25L7.88 8.13L6.46 9.55L12 15Z" />
      </svg>
    `;

    customButton.addEventListener('click', function () {
      console.log('Custom button clicked!');
    });

    // Insert before search button
    searchButton.parentNode.insertBefore(customButton, searchButton);
  }
});
