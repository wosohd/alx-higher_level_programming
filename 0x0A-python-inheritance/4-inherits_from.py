#!/usr/bin/python3
"""Defines the inherits_from function."""


def inherits_from(obj, a_class):
    """
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
