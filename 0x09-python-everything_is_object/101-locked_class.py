#!/usr/bin/python3
"""Represents a locked class"""


class LockedClass:
    """This class prevents new objects/instances to be created
    else its name is "first_name"""

    __slots__ = ["first_name"]
