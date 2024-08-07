document.addEventListener('DOMContentLoaded', () => {
  try {
    const headerElement = document.querySelector('HEADER');
    if (headerElement) {
      headerElement.style.color = '#FF0000';
    } else {
      console.error('Header element not found');
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
});

