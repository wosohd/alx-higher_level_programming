#!/usr/bin/python3
"""Defines a class MyInt."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """what was != is now ==."""
        return self.real != value

    def __ne__(self, value):
        """what was == is now !=."""
        return self.real == value
