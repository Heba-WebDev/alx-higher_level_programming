#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const users = {};

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (task?.completed) {
      if (users[task?.userId]) {
        users[task?.userId]++;
      } else {
        users[task?.userId] = 1;
      }
    }
  }
  console.log(users);
});
