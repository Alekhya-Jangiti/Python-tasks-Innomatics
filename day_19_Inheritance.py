
# 1. Create an Animal class with a method to eat. Create a Dog class that inherits from Animal .

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
# d1 = Dog()
# d1.eat()
# d1.bark()

# 2. Create a Person class with a method to display the name. Create a Student class that inherits from Person.

# class Person:
#     def name(self):
#         print("Name: Alekhya")

# class Student(Person):
#     def course(self):
#         print("Course: Python")
# s1 = Student()
# s1.name()
# s1.course()

# 3. Create a Shape class with a method to display the shape. Create a Square class that inherits from Shape.

# class Shape:
#     def display(self):
#         print("This is a shape")

# class Square(Shape):
#     def area(self):
#         side = 5
#         print("Area =", side * side)
# s1 = Square()
# s1.display()
# s1.area()

# 4. Create three classes Animal, Dog, and Puppy using multilevel inheritance. Each class should have its own method.

# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class Puppy(Dog):
#     def play(self):
#         print("Puppy is playing")
# p1 = Puppy()
# p1.eat()
# p1.bark()
# p1.play()

# 5. Create three classes Person, Student, and Graduate using multilevel inheritance. Each class should have its own method.

# class Person:
#     def display_person(self):
#         print("Person details")
        
# class Student(Person):
#     def study(self):
#         print("Student is studying")
        
# class Graduate(Student):
#     def complete(self):
#         print("Graduation completed")
# g1 = Graduate()
# g1.display_person()
# g1.study()
# g1.complete()

# 6. Create three classes Vehicle, Car, and SportsCar using multilevel inheritance. Each class should have its own method.

class Vehicle:
    def start(self):
        print("Vehicle is started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class SportsCar(Car):
    def race(self):
        print("Sports car is racing")
s1 = SportsCar()
s1.start()
s1.drive()
s1.race()
