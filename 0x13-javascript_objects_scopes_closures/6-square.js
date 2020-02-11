#!/usr/bin/node
/* class Square inheriting from the previous class Square */
const firstSquare = require('./5-square');

module.exports = class Square extends firstSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log('c'.repeat(this.width));
      }
    }
  }
};
