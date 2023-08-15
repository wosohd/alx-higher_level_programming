#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let j = 0; j < list.length; j++) {
    count = (list[j] === searchElement ? count + 1 : count);
  }

  return count;
};
