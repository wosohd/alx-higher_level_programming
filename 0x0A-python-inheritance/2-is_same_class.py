#!/usr/bin/python3
"""Defines the function is_same_class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Returns:true if obj is the exact class a_class, otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
