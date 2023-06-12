#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """raises an exception when called."""
        raise Exception("area() is not implemented")
