#!/usr/bin/python3
"""Square Class
A Square Class
"""


class Square:
    """Square Class
    A Square Class
    """
    
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square object with given size and position
        :param size: an integer representing the size of the square. Default is 0
        :param position: a tuple of 2 positive integers representing the position
        of the square. Default is (0, 0)
        :raises TypeError: if size is not an integer
        :raises ValueError: if size is less than 0
        :raises TypeError: if position is not a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square
        :return: an integer representing the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        :param value: an integer representing the new size of the square
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square
        :return: a tuple of 2 positive integers representing the position
        of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square
        :param value: a tuple of 2 positive integers representing the new
        position of the square
        :raises TypeError: if value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Get the area of the square
        :return: an integer representing the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square to the console using the character '#'
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
    def __str__(self):
        return self.my_print()
       
