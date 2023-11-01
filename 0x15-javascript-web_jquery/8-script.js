const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.ajax({
    url: URL,
    method: "GET",
    dataType: "json",
    success: function(data) {
      for(let i = 0; i < data?.results.length; i++) {
        $("#list_movies").append(`<li>${data?.results[i]?.title}</li>`)
      }
    },
    error: function(xhr, status, error) {
      console.error("Request failed: " + status + " - " + error);
    }
  });
