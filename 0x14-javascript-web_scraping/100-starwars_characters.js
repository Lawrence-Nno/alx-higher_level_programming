#!/usr/bin/mode
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (_error, _response, body) {
  const characters = JSON.parse(body).characters;

  for (let a = 0; a < characters.length; ++a) {
    request(characters[a], function (_cError, _cResponse, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
