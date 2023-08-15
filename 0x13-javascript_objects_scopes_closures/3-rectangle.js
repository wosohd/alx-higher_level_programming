#!/usr/bin/node
/**
 * Defines rectangle class with w and h attr.
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let myVar = '';
      let z = 0;
      while (z < this.width) {
        myVar += 'X';
        z++;
      }

      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
