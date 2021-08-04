#!/usr/bin/node
// Imports an array and computes a new array.

const arr = require('./100-data').list;
const arr2 = arr.map((value, index) => value * index);

console.log(arr);
console.log(arr2);
