class Rectangle:
    def __init__(self, width,  height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = ''
        for _ in range(self.height):
            for _ in range(self.width):
                pic += '*'
            pic += '\n'
        return pic

    def get_amount_inside(self, shape):
        rows = self.height // shape.height
        cols = self.width // shape.width
        return rows * cols

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f'Square(side={self.height})'
