#!/usr/bin/python3
"""a class square"""


class Square:
    """Derives a square """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(isinstance(v, int) for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates the area of a square
        Returns: area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """Gets the value of `size`"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of `size`
        Args:
            value (int): value to be set to `size`
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Gets `position` value """
        return self.__position

    @position.setter
    def position(self, value):
        """Puts the value of `position`
        Args:
            value (int): value to be set to `position` attribute
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints a square using the character #"""
        if self.__size == 0:
            print()
            return

        [print() for i in range(self.position[1])]
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
