#!/usr/bin/python3
from models.base import Base
"""A class that inherits from Base"""


class Rectangle(Base):
    """A class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Rectangle constructor to initialise an instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """A getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute and Exceptions"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """A getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute and Exceptions"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """A getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute and Exceptions"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """A getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute and Exceptions"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """This func prints the triangle in the stdout using #"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """The string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """This method assigns arguments to each attribute"""
        if args and len(args) != 0:
            a = 0
            for attr in args:
                if a == 0:
                    if attr is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = attr
                elif a == 1:
                    self.width = attr
                elif a == 2:
                    self.height = attr
                elif a == 3:
                    self.x = attr
                elif a == 4:
                    self.y = attr
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """This method returns the dictionary representation of the class"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

