#!/usr/bin/python3
"""Derive a bytecode Magic class"""

import math


class MagicClass:
    def __init__(self, radius=0):
        """Initilize Magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area of Magic class"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumference Magic class"""
        return 2 * math.pi * self.__radius
