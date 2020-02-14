/* fetches and lists all movies titles */
$.get('https://swapi.co/api/films/?format=json', (res) => {
  for (const movie of res.results) {
    $('#list_movies').append($('<li></li>').text(movie.title));
  }
});
