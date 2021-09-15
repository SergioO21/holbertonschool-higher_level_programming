#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (err, res, body) {
  if (err) { console.log(err); }

  const data = JSON.parse(body);
  let id = 1;
  const task = {};

  for (let i = 0; i < data.length; i++) {
    if (data[i].userId === id) {
      task[id] = 0;
      id += 1;
    }
  }

  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      task[data[i].userId] += 1;
    }
  }
  console.log(task);
});
