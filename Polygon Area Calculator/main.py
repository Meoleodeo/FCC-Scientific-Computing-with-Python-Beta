class Rectangle:
    def __init__(self, width, height):
        self.width = width 
        self.height = height 

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ''
            for _ in range(self.height):
                picture += "*" * self.width + '\n'
            return picture

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_amount_inside(self, shape):
        if shape.width <= self.width and shape.height <= self.height:
            return (self.height // shape.height) * (self.width // shape.width)
        else:
            return 0


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self.width})"


# Testing the classes
rect = Rectangle(5, 10)
print(rect.get_area())        # Output: 50
rect.set_width(3)
print(rect.get_perimeter())   # Output: 26
print(rect)                   # Output: Rectangle(width=3, height=10)

sq = Square(9)
print(sq.get_area())          # Output: 81
sq.set_side(4)
print(sq.get_diagonal())      # Output: 5.656854249492381
print(sq)                     # Output: Square(side=4)

# Modifying Square using set_width and set_height
sq.set_width(5)
print(sq)                     # Output: Square(side=5)

sq.set_height(6)
print(sq)                     # Output: Square(side=6)
