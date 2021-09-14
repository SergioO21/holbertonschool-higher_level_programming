#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (err, res, body) {
  let count = 0;

  if (err) { console.log(err); }

  const wedgeAntille = 'https://swapi-api.hbtn.io/api/people/18/';
  const data = JSON.parse(body);

  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes(wedgeAntille)) {
      count += 1;
    }
  }

  console.log(count);
});
