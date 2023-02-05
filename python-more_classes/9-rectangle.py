#!/usr/bin/python3
"""
    Class Rectangle
"""


class Rectangle:
    """
        Empty class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        aux = self.__width
        if type(aux) is not int:
            raise TypeError("width must be an integer")
        if aux < 0:
            raise ValueError("width must be >= 0")
        Rectangle.number_of_instances += 1

    def __str__(self, width=0, height=0):
        high = self.__height
        large = self.__width
        if high == 0:
            return ""
        if large == 0:
            return ""
        for y in range(high):
            if y == 0:
                pass
            else:
                print()
            for x in range(large):
                print(str(self.print_symbol), end="")
        return ""

    def __repr__(self, width=0, height=0):
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self, width=0, height=0):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        aux = self.__width
        if type(aux) is not int:
            raise TypeError("width must be an integer")
        if aux < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        return (self.width + self.height) * 2

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
