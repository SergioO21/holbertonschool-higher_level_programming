#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (err, res, body) {
  if (err) { console.log(err); }

  const data = JSON.parse(body);
  const taskCompleted = {};

  for (const task of data) {
    if (task.completed === true) {
      if (task.userId in taskCompleted) {
        taskCompleted[task.userId] += 1;
      } else {
        taskCompleted[task.userId] = 1;
      }
    }
  }
  console.log(taskCompleted);
});
