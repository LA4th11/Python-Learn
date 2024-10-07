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