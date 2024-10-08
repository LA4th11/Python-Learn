""" Exercise 1: Basic Inheritance
Create a base class called Animal that has the following:

Attribute: name
Method: make_sound() that prints "Some sound".
Now, create two subclasses Dog and Cat that inherit from the Animal class. Each subclass should override the make_sound() method:

The Dog class should print "Bark".
The Cat class should print "Meow".
Task: Create an instance of each class (Dog and Cat) and call their make_sound() methods.

Exercise 2: Adding New Attributes in Subclass
Create a class called Vehicle with:

Attributes: brand and year.
Method: start_engine() that prints "Engine started."
Now, create a subclass Car that inherits from Vehicle and adds a new attribute doors (number of doors). Override the start_engine() method to print "Car engine started."

Task: Create an instance of the Car class, provide the values for brand, year, and doors, and call the start_engine() method.

Exercise 3: Using super() to Extend Functionality
Create a base class called Person with:

Attributes: first_name and last_name.
Method: introduce() that prints "Hi, I'm first_name last_name."
Now, create a subclass Student that inherits from Person and adds a new attribute student_id. The introduce() method should be extended to also print "My student ID is student_id."

Task: Create an instance of the Student class, provide the values for first_name, last_name, and student_id, and call the introduce() method. """
# -----------------------------------------------------------------------------#
# BASIC INHERITANCE:EXERCISE 1 <----------
""" class Animal:
  def __init__(self, name):
    self.name = name
    
  def make_sound():
    print("Some sound")
    
class Dog(Animal):
  def make_sound(self):
    print(F"The {self.name} sound \"Bark\"")

class Cat(Animal):
  def make_sound(self):
    print(F"The {self.name} sound \"Meow\"")

if __name__ == "__main__":
  dog = Dog("Dog")
  cat = Cat("Cat")
  
  Dog.make_sound(dog)
  Cat.make_sound(cat) """

# ADDING NEW ATTRIBUTES IN SUBCLASS:EXERCISE 2 <----------
""" class Vehicle:
  
  def __init__(self, brand, year):
    self.brand = brand
    self.year = year
  
  def start_engine(self):
    print(F"#VEHICLE:\nBrand: {self.brand}\nYear: {self.year}")
    print("Engine Started.")

class Car(Vehicle):
  
  def __init__(self, brand, year, doors):
    super().__init__(brand,year)
    self.doors = doors
  
  def start_engine(self):
    print(F"\n#CAR:\nBrand: {self.brand}\nYear: {self.year}\nDoors: {self.doors}")
    print("Car engine started.")
    
if __name__ == "__main__":
  vehicle = Vehicle("Honda", 2010)
  car = Car("Honda", 2010, 4)
  
  Vehicle.start_engine(vehicle)
  Car.start_engine(car) """

# USIMG super() TO EXTEND FUNCTIONALITY:EXERCISE 3 <----------
""" class Person:
  
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    
  def introduce(self):
    print(F"Hi, I'm {self.first_name} {self.last_name}")
    
class Student(Person):
  
  def __init__(self, first_name, last_name, student_id):
    super().__init__(first_name, last_name)
    self.student_id = student_id

  def introduce(self):
    super().introduce()
    print(F"My student ID is {self.student_id}")
    
if __name__ == "__main__":
  student = Student("Lorenzo", "Laforteza", 201915547)
  
  Student.introduce(student) """