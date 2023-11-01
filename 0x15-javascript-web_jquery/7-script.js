const URL =  'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.ajax({
    url: URL,
    method: "GET",
    dataType: "json",
    success: function(data) {
      if(data?.name) {
        $("#character").text(data?.name)
      }
    },
    error: function(xhr, status, error) {
      console.error("Request failed: " + status + " - " + error);
    }
  });
