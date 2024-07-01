class Rectangle:
    """This is a rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize the Rectangle instance
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrieves a width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting a width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves a height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting a height of the rectangle with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return a rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """return the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """drawing the rectangle in the form of #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        x = ""
        for i in range(self.__height):
            if i < self.__height - 1:
                x += ("#" * self.__width) + "\n"
            else:
                x += ("#" * self.__width)
        return x
