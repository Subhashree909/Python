class Person:
  def _init_(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("John", 30)
print(p._dict_)

print(help(Person))