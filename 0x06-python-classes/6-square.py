#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
    
    def my_print(self):
        """returns the square in the form of hash '#'"""

        if self.__size == 0:
            print()
        else:
            for i in range(1, self.area() + 1):
                if self.__position[1] <= 1:
                    if i % self.__size == 1:
                        for j in range(0, (self.__position[0])):
                            print(" ", end="")

                print("#", end="")
                if i % self.__size == 0:
                    print()
    
    @property
    def position(self):
        """Return position"""

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or (value[0] or value[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
