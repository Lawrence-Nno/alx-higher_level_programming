#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, _response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = {};
    body = JSON.parse(body);

    for (let a = 0; a < body.length; ++a) {
      const userId = body[a].userId;
      const completed = body[a].completed;

      if (completed && !completedTasks[userId]) {
        completedTasks[userId] = 0;
      }
      if (completed) ++completedTasks[userId];
    }
    console.log(completedTasks);
  }
});
