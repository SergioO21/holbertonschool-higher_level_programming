#!/usr/bin/node
// Prints two arguments passed to it, in the following format: “ is ”.
const process = require('process');
const args = process.argv;

console.log(args[2] + ' is ' + args[3]);
