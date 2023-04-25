#!/usr/bin/mode
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, response, body) {
if (!err) {
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, function (err, response, body) {
      if (!err) {
        console.log(JSON.parse(body).name);
       }
     });
   });
  }
});
