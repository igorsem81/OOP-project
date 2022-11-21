
class Student:
    "This is a student class"
    age = 16
    def get_name(self):
        print('Cyber')

student = Student()
print(student.age)
print(student.get_name())

#Create an animal class, with the following properties:
#•name
#•age
#•hunger

#Create the following methods for Animal class:
#•get_name returns the name of the animal
#•get_age returns the age of the animal
#•is_hungry return if the animal is hungry or not (any value above 0 is hungry)
#•feed decrease the value of hunger in one point (until zero)

class Animal:
    def name(self):
        print('name is rocki')
    def get_age(self):
        print("age", 4)
    def is_hungry(self):
        print('hungry')

dog = Animal()

print(dog.name())
print(dog.get_age())
print(dog.is_hungry())

# Constructer
class Student1:
    "This is a student class"
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def get_name(self):
        return self.name

student = Student1('Moshe', 16, '123123')
print(student.get_name())

# Create a constructor for Animal class
# Create a new class called Zoo and set the following
#functions:
# • load_animals get a CSV file and creates animals by the loaded data
# • add_animal
# • remove_animal
# • show_animals

class Animal():
    "This is a Animal class"
    def __init__(self, weight, color, kind):
        self.weight = weight
        self.color = color
        self.kind = kind
    def get_kind(self):
        return self.kind

