#!/usr/bin/python3
"""This func defines an inherited list class MyList."""


class MyList(list):
    """This class inherits from class list"""

    def print_sorted(self):
        """Prints a sorted self"""
        print(sorted(self))
