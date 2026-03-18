from abc import ABC, abstractmethod

# Define the Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

# Concrete classes implementing abstract methods
class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * (self.r**2)
    def perimeter(self): return 2 * 3.14 * self.r

# Usage
rect = Rectangle(4, 7)
circ = Circle(5)
print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circ.area()}")
