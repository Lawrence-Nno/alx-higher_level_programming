#!/usr/bin/python3
"""A class representation of a Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor that initializes each instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The getter returns a size of the square since all sides are equal"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This method updates the attributes of the class"""
        if args and len(args) != 0:
            a = 0
            for attr in args:
                if a == 0:
                    if attr is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = attr
                elif a == 1:
                    self.size = attr
                elif a == 2:
                    self.x = attr
                elif a == 3:
                    self.y = attr
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """This method returns the dictionary representation of the class"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """The String representation of the square class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
