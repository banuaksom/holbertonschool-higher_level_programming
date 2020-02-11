#!/usr/bin/node
/* returns the reversed version of a list */
exports.esrever = function (list) {
  let temp;

  for (let first = 0, last = list.length - 1; first < last; first++, last--) {
    temp = list[first];
    list[first] = list[last];
    list[last] = temp;
  }
  return (list);
};
