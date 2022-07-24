class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width*height

w = int(input())
h = int(input())

print(Shape.area(w, h))