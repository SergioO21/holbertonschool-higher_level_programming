#!/usr/bin/node
// Prints a square.
const process = require('process');
const args = process.argv;

if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('X'.repeat(parseInt(args[2])));
  }
}
