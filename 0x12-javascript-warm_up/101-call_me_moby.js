#!/usr/bin/node
/**
 * export
 */

exports.callMeMoby = function (x, theFunction) {
  for (let i = x; i > 0; i--) {
    theFunction();
  }
};
