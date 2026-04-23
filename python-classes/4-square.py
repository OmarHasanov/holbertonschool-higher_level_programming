#!/usr/bin/python3
"""This module defines a Square class with property getter and setter."""


class Square:
    """This class represents a square with controlled size access."""

    def __init__(self, size=0):
        """Initialize a square with optional size."""
        self.size = size  # setter istifadə olunur

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): size of the square.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
