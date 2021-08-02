#!/usr/bin/node
// Computes and prints a factorial.
const process = require('process');
const args = process.argv;

if (isNaN(parseInt(args[2]))) {
  console.log(1);
} else {
  console.log(factorial(parseInt(args[2])));
}

function factorial (n) {
  if (n === 0) {
    return (1);
  }
  return n * factorial(n - 1);
}
