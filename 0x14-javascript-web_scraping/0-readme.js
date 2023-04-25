#!/usr/bin/node
const file = require('file');
file.readFile(process.argv[2], 'utf8', function (err, data) {
  console.log(err || data);
});
