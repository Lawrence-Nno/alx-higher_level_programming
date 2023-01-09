#!/usr/bin/python3
"""This class defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """THis func checks if an object is an instance or inherited instance of a class
    and returns True otherwise False
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to."""
    if isinstance(obj, a_class):
        return True
    return False
