#!/usr/bin/node
// Returns the number of occurrences in a list.

exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      ocurrences += 1;
    }
  }

  return ocurrences;
};
