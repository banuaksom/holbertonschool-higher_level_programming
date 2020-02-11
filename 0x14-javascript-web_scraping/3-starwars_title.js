#!/usr/bin/node
/* prints title of Star Wars movie under given integer */
const request = require('request');

request.get(`http://swapi.co/api/films/${process.argv[2]}/`,
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).title);
  });
