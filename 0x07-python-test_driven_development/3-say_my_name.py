#!/usr/bin/python3

"""A function that prints first and last names"""


def say_my_name(first_name, last_name=""):
    """This function prints first name and last name only if they are both strings

    raises:
        raises a TypeError if either of them isn't a string.

    return:
        returns a string with the full name"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
