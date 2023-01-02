#!/usr/bin/python3
class Rectangle:
    """This class represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value"""
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if not isinstance(int, value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
