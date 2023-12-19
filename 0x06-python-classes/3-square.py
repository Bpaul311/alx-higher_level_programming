i#!/usr/bin/python3

class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """
        Initializes a new square with the specified size.

        Args:
        - size (int): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns: int: The area of the square.
        """
        return self.__size * self.__size

