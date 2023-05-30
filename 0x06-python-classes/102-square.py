#!/usr/bin/python3
"""a class square"""


class Square:
    """Derives a square """
    def __init__(self, size=0):
        """Initializes the data
        Args:
            size (int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def __lt__(self, other):
        """Define the < comparison to a Square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Define the == comparision to a Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the > comparison to a Square"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square"""
        return self.area() >= other.area()

    def area(self):
        """Calculates the area of a square
        Returns: the area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """gets the value of `size`"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of `value`
        Args:
            value (int): value to be set to `value`
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value
