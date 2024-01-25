class Employee:
  def _init_(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def _init_(self, name, id, lang):
    super()._init_( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)