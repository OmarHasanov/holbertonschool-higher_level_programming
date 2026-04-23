#!/usr/bin/python3
"""This module defines a Square class with printing capability."""


class Square:
    """This class represents a square with size, area, and print method."""

    def __init__(self, size=0):
        """Initialize a square with optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # characters."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
