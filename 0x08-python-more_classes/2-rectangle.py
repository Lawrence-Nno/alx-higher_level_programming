#!/usr/bin/python3
"""This class defines a Rectangle"""


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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method calcs the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This method returns the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
