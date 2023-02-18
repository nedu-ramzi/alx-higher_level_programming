#!/usr/bin/python3
""" defines Square class, inherits from Rectangle class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the Square instance attributes """
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
        idx = 0
        for arg in args:
            if idx == 0:
                self.id = arg
            elif idx == 1:
                self.size = arg
            elif idx == 2:
                self.x == arg
            elif idx == 3:
                self.y = arg
            idx += 1

    def to_dictionary(self):
        """ returns the dictionary representation of
        all the instances of square """
        sq_dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
        return sq_dict

    def __str__(self):
        """ returns the string representation of Square instance """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
