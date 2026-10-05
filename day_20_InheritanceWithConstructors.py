
# 1. Hierarchical without constructor

# class Payment:
#     def payment_status(self):
#         print("Payment is being processed")
# class UPI(Payment):
#     def upi_payment(self):
#         print("Payment through UPI")
# class Card(Payment):
#     def card_payment(self):
#         print("Payment through Card")
# u1 = UPI()
# u1.payment_status()
# u1.upi_payment()
# c1 = Card()
# c1.payment_status()
# c1.card_payment()

# 2. Hierarchical with constructor and super()

# class Shape:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print("Shape =", self.name)
# class Square(Shape):
#     def __init__(self, name, side):
#         super().__init__(name)
#         self.side = side
#     def area(self):
#         print("Square Area =", self.side * self.side)
        
# class Rectangle(Shape):
#     def __init__(self, name, length, breadth):
#         super().__init__(name)
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         print("Rectangle Area =", self.length * self.breadth)

# s1 = Square("Square", 5)
# s1.display()
# s1.area()

# r1 = Rectangle("Rectangle", 10, 5)
# r1.display()
# r1.area()

# 3. hybrid inheritance without constructor

# class College:
#     def college_details(self):
#         print("College: JNTUH")

# class Student(College):
#     def study(self):
#         print("Student is studying")

# class Employee(College):
#     def work(self):
#         print("Employee is working")

# class WorkingStudent(Student, Employee):
#     def manage(self):
#         print("Student is studying and working")

# w1 = WorkingStudent()

# w1.college_details()
# w1.study()
# w1.work()
# w1.manage()

# 4. hybrid inheritance with constructor ans super()

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

# class Electric(Vehicle):
#     def __init__(self, brand, battery):
#         super().__init__(brand)
#         self.battery = battery

# class ElectricCar(Car, Electric):
#     def __init__(self, brand, model, battery):
#         Vehicle.__init__(self, brand)
#         self.model = model
#         self.battery = battery

#     def display(self):
#         print("Brand =", self.brand)
#         print("Model =", self.model)
#         print("Battery =", self.battery)

# e1 = ElectricCar("Tesla", "Model 3", "75 kWh")
# e1.display()

# 5. multiple inheritance without constructor

# class Batting:
#     def batting(self):
#         print("Player is batting")

# class Bowling:
#     def bowling(self):
#         print("Player is bowling")

# class AllRounder(Batting, Bowling):
#     def playing(self):
#         print("Player is an All-Rounder")

# p1 = AllRounder()

# p1.batting()
# p1.bowling()
# p1.playing()

# 6. multiple inheritance with constructor and super() 

class Father:
    def __init__(self, name, hobby):
        super().__init__(hobby=hobby)
        self.name = name

class Mother:
    def __init__(self, hobby):
        self.hobby = hobby

class Child(Father, Mother):
    def __init__(self, name, hobby):
        super().__init__(name, hobby)

    def display(self):
        print("Name =", self.name)
        print("Hobby =", self.hobby)

c1 = Child("Rahul", "Cricket")
c1.display()
