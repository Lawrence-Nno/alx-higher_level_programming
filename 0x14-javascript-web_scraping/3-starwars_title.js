#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.alx-tools.com/api/' + process.argv[2];
request(url, function (err, response, body) {
  console.log(error || JSON.parse(body).title);
});
