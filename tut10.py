#strings are immutible
a= "!!!Baishakhi! !!! Baishakhi"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Baishakhi","Darshani"))
print(a.split(" "))
blogHeading = "introduction to jS"
print(blogHeading.capitalize())

str1="Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Baishakhi"))

str1="Welcome to the console!!!"
print(str1.endswith("!!!"))

str1="Welcome to the console!!!"
print(str1.endswith("to",4,10))

str1="He's name is Muna. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1="WelcomeToTheConsole"
print(str1.isalnum())

str1="WelcomeToTheConsole"
print(str1.isalpha())

str1="hello world"
print(str1.islower())

str1="We wish you a Merry Christmas\n"
print(str1.isprintable())

str1="          "
print(str1.isspace())
str2="          "
print(str2.isspace())

str1="World Health Organisation"
print(str1.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Muna. Muna is an honest man."
print(str1.title())



