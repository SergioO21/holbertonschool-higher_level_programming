#!/usr/bin/node

const request = require('request');
const argv = process.argv.slice(2);
const url = `https://swapi-api.hbtn.io/api/films/${argv[0]}`;

request(url, function (err, res, body) {
  if (err) { console.log(err); }
  console.log(JSON.parse(body).title);
});
