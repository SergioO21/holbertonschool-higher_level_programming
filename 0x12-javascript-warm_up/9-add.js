#!/usr/bin/node
// Prints the addition of 2 integers.
const process = require('process');
const args = process.argv;

if (isNaN(parseInt(args[2])) | isNaN(parseInt(args[3]))) {
  console.log('NaN');
} else {
  console.log(parseInt(args[2]) + parseInt(args[3]));
}
