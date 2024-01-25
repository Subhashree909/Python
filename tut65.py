class Shape:
  def _init_(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y

class Circle(Shape):
    def _init_(self, radius):
      self.radius = radius
      super()._init_(radius, radius)

    def area(self):
        return 3.14 *  super().area()
      
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())