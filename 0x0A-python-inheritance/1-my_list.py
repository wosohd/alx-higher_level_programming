#!/usr/bin/python3
"""Defines class MyList."""


class MyList(list):
    """class inheriting from list."""

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
