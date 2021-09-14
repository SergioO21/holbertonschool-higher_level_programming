#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (err, res, body) {
  if (err) { console.log(err); }

  fs.writeFile(argv[1], body, err => {
    if (err) { console.error(err); }
  });
});
