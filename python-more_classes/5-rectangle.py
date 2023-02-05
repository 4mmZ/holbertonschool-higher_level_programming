"""
    Class Rectangle
"""


class Rectangle:
    """
        Empty class
    """
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
                print("#", end="")
        return ""

    def __repr__(self, width=0, height=0):
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self, width=0, height=0):
        print("Bye rectangle...")
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
