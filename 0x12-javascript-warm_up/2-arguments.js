#!/usr/bin/node
// Prints a message depending of the number of arguments passed.
const process = require('process');
const args = process.argv;

if (args.length < 3) {
  console.log('No argument');
} else if (args.length > 3) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
