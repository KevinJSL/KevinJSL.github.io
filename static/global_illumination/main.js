// Function to fetch and insert an HTML component (like navigation or footer)
async function loadComponent(url, targetElementId, selector) {
    try {
        const response = await fetch(url);
        const data = await response.text();

        // Create a temporary DOM element to parse the fetched HTML
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = data;

        // Extract the element (nav or footer)
        const component = tempDiv.querySelector(selector);
        if (component) {
            document.getElementById(targetElementId).appendChild(component);
        } else {
            console.error(`No ${selector} found in the component HTML.`);
        }
    } catch (error) {
        console.error('Error loading component:', error);
    }
}

// Load navigation and footer components
document.addEventListener('DOMContentLoaded', () => {
    loadComponent('/static/global_illumination/component.html', 'nav-bar', 'nav');
    loadComponent('/static/global_illumination/component.html', 'foot', 'footer');
});

const hamburgerIcon = document.getElementById('hamburger-icon');
const mobileDropdown = document.getElementById('mobile-dropdown');

// Toggle the visibility of the dropdown when the hamburger icon is clicked
hamburgerIcon.addEventListener('click', () => {
    mobileDropdown.classList.toggle('hidden');
});
