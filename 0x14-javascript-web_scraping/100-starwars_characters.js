#!/usr/bin/node
/* prints all characters of a Star Wars movie */
const request = require('request');

request(`https://swapi.co/api/films/${process.argv[2]}/`,
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    for (const char of JSON.parse(body).characters) {
      request(char, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  });
