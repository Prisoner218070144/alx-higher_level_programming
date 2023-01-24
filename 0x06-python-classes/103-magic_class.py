#!/usr/bin/python3
import dis
import math

"""
A class that represents a circle with a given radius
"""


class MagicClass:
    """
    A class that represents a circle with a given radius
    """
    def __init__(self, radius=0):
        """
        Initialize a new MagicClass object with given radius
        :param radius: a number representing the radius of the circle.
        Default is 0.
        :raises TypeError: if radius is not a number
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Get the area of the circle
        :return: a float representing the area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Get the circumference of the circle
        :return: a float representing the circumference of the circle
        """
        return 2 * math.pi * self.__radius
