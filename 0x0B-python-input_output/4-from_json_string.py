#!/usr/bin/python3
"""Returns an object (Python data structure)
represented by a JSON string"""

import json


def from_json_string(my_str):
    """Returns Object"""
    return json.loads(my_str)
