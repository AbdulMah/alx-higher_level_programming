$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response, status) {
    if (status === 'success') {
      const films = response.results;
      for (const idx in films) {
        $('UL#list_movies').append('<li>' + films[idx].title + '</li>');
      }
    }
  });
});
