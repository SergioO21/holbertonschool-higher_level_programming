#!/usr/bin/node
// Prints the first argument passed to it.
const process = require('process');
const args = process.argv;

if (typeof args[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(args[2]);
}
