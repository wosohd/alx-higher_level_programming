#!/usr/bin/python3
"""Defines the "from_json_string" function."""
import json


def from_json_string(my_str):
    """Return object representation of a JSON string."""
    return json.loads(my_str)
