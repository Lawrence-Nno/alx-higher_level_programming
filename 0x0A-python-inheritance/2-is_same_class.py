#!/usr/bin/python3
"""A class-checking function."""


def is_same_class(obj, a_class):
    """THis func checks if an object is exactly an instance of a given class.
    returns True is it is, otherwise false.
    Args:
        obj (any type): The object to check.
        a_class (type): The class to match the type of obj to
    """
    if type(obj) == a_class:
        return True
    return False
