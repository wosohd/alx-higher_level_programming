#!/usr/bin/python3
"""Defines an object lookup function"""

def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
