#!/usr/bin/node
/* prints the number of arguments and value */
let num = 0;
exports.logMe = function (item) {
  console.log('%d: %s', num, item);
  num++;
};
