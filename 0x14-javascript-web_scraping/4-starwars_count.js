#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (err, res, body) {
  if (err) { console.log(err); }

  let count = 0;
  const data = JSON.parse(body);
  const wedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';

  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes(wedgeAntilles)) {
      count++;
    }
  }
  console.log(count);
});
