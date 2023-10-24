#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(path, body, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
