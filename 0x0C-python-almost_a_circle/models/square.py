#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        if args:
            names = ['id', 'size', 'x', 'y']
            for i, values in enumerate(args):
                if i < len(names):
                    setattr(self, names[i], values)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        d = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
        return d
