import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage:
circle = Circle(5)
print(circle.area()) #The output has 78.53981634