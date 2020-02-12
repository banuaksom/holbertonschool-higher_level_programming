#!/usr/bin/node
const request = require('request');

const dicti = {};

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (dicti[task.userId]) {
        dicti[task.userId]++;
      } else {
        dicti[task.userId] = 1;
      }
    }
  }
  console.log(dicti);
});
