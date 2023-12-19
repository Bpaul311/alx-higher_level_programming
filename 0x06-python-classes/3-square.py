i#!/usr/bin/python3

class Square:
    """
    This class represents a square.

    Attributes:
    - size (int): The size of the square.

    Methods:
    - __init__(self, size=0): Initializes a new square with the specified size.
    - area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square with the specified size.

        Parameters:
        - size (int): The size of the square. Default is 0.

        Raises:
        - TypeError: If the size is not an integer.
        - ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size * self.__size

