$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const films = data.results;

    for (const film in films) {
      $('UL#list_movies').append('<li>' + films[film].title + '</li>');
    }
  });
});
