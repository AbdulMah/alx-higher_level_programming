#!/usr/bin/node
/**
 * export
 */

exports.addMeMaybe = function (number, theFunction) {
  return (theFunction(number + 1));
};
