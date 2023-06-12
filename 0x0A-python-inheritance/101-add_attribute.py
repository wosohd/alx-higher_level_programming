#!/usr/bin/python3
""" Defines a function that adds attributes to objects"""


def add_attribute(a_class, name, value):
    """ Adds a new attribute to an object if it’s possible """
    if hasattr(a_class, "__dict__"):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")
