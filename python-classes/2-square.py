#!/usr/bin/python3
"""This module defines a Square class with size validation."""


class Square:
    """This class represents a square with a validated size."""

    def __init__(self, size=0):
        """Initialize a square with optional size.

        Args:
            size (int): size of the square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
