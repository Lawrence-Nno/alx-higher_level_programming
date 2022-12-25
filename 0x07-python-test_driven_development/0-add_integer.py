#!/usr/bin/python3
""" This is an integer addition function."""


def add_integer(a, b=98):
    """ In this add function, input parameters must be an integer or a float. 
    The float will first be casted into an integer before any addition is done

    args:
        a: (int or float) is the first parameter
        b: (int or float) is the second parameter defaulted to 98

    Return:
        Returns an int, the result of the addition.

    Raises:
        Raises a TypeError if input isn't an int or float. """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

