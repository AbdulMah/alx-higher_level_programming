#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((lastValue, currentValue) => currentValue === searchElement ? lastValue + 1 : lastValue, 0);
};
