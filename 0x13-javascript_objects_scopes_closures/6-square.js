#!/usr/bin/node
/**
 * Class super that inherits from square class 5-square.js
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let j = 0; j < this.height; j++) {
      let myVar = '';
      let z = 0;
      while (z < this.width) {
        myVar += myChar;
        z++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
