#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile(argv[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
