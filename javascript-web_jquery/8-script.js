//Updates
$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    const result = data["results"]
    for (title in result) {
        $("#list_movies").append($("<li>").text(result[title]["title"]));
    }
});