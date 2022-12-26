#!/usr/bin/python3

"""A function that prints a square using #"""


def print_square(size):
    """This function prints a square using the symbol '#'
    arg:
        size (int): the sumber of '#'s to print
    raises:
        TypeError: if size isn't an int
        TypeError: if size is less than 0
        TypeError: if size is a float and is less than 0
    return:
        A square with equal number of '#' on each side"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for i in range(size):
            print("#",end="")
        print()
