import logging
import argparse

class NegativeValueError(ValueError):
    pass


class Rectangle:
    logging.basicConfig(filename="./log",
                        level=logging.INFO,
                        encoding='utf-8',
                        format='{levelname:<5}, asctime.now(), time:{asctime}, {msg}',
                        style='{')



    def __init__(self, width, height=None):
        if width <= 0:
            logger = logging.getLogger()
            logger.error('NegativeValueError')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger = logging.getLogger()
                logger.error('NegativeValueError')
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            logger = logging.getLogger()
            logger.error('NegativeValueError')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            logger = logging.getLogger()
            logger.error('NegativeValueError')
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

# rectangle = Rectangle(2,-15)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('width', type=float)
    parser.add_argument('--height', type=float)

    args = parser.parse_args()
    try:
        rectangle = Rectangle(args.width, args.height)
        print(f"Rectangle created with width: {rectangle.width}, height: {rectangle.height}")
    except NegativeValueError as e:
        print(e)


