class Employee:
  def _init_(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def _init_(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def _init_(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())