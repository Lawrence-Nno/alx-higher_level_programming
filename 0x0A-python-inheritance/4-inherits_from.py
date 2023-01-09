#!/usr/bin/python3
"""This class defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """This func checks if an object is an inherited instance of a class
    and returns True, otherwise False
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
