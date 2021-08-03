#!/usr/bin/node
// Returns the reversed version of a list.

exports.esrever = function (list) {
  const reverList = [];

  for (let i = (list.length - 1); i >= 0; i--) {
    reverList.push(list[i]);
  }

  return reverList;
};
