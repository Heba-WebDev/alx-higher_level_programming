#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const res = JSON.parse(body);
  const charachters = res?.characters;
  for (const character of charachters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
