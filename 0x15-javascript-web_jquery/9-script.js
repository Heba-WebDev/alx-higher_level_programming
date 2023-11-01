const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.ajax({
    url: URL,
    method: "GET",
    dataType: "json",
    success: function(data) {
      if (data?.hello) {
        $("#hello").text(data?.hello)
      }
    },
    error: function(xhr, status, error) {
      console.error("Request failed: " + status + " - " + error);
    }
  });
