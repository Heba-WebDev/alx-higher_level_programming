#!/usr/bin/node

const request = require('request-promise-native');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      printCharacters(characters, index + 1);
    }
  });
}
