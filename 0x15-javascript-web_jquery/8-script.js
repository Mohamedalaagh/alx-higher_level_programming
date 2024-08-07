(async () => {
  try {
    const response = await fetch('https://swapi.co/api/films/?format=json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    const moviesList = data.results.map(movie => `<li>${movie.title}</li>`).join('');
    document.querySelector('UL#list_movies').innerHTML = moviesList;
  } catch (error) {
    console.error('Failed to fetch movies:', error);
  }
})();
