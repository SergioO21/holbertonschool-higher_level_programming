#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

fs.writeFile(argv[0], argv[1], err => {
  if (err) {
    console.error(err);
  }
});
