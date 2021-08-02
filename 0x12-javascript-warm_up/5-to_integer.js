#!/usr/bin/node
/* Prints My number: <first argument converted in integer>
 * If the first argument can be converted to an integer.
 */
const process = require('process');
const args = process.argv;

if (isNaN(parseInt(args[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
