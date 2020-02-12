#!/usr/bin/node
/* prints number of movies with “Wedge Antilles” */
const request = require('request');
let counter = 0;

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const movie of JSON.parse(body).results) {
    for (const character of movie.characters) {
      if (character.includes('18')) {
        counter++;
      }
    }
  }
  console.log(counter);
});
