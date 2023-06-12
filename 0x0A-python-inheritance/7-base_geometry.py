#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """raises an exception when called."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter is an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
