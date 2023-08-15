#!/usr/bin/node
/**
 * Class super that inherits from rectangle class 4-rectangle.js
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
