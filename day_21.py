
# 1. Write a Python program to demonstrate polymorphism by passing different objects to the same function to calculate their respective payments.

# class UPI:
#     def pay(self, amount):
#         print("UPI Payment =", amount)

# class Card:
#     def pay(self, amount):
#         print("Card Payment =", amount)

# def process_payment(payment, amount):
#     payment.pay(amount)

# process_payment(UPI(), 1000)
# process_payment(Card(), 2000)

# 2. Write a Python program to demonstrate polymorphism by using the same area() method in Square and Rectangle classes.

# class Square:
#     def area(self):
#         side = 5
#         print("Square Area =", side * side)

# class Rectangle:
#     def area(self):
#         length = 10
#         breadth = 5
#         print("Rectangle Area =", length * breadth)

# s1 = Square()
# r1 = Rectangle()

# s1.area()
# r1.area()

# 3. Write a Python program to demonstrate method overriding using Animal and Dog classes.

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# a1 = Animal()
# d1 = Dog()

# a1.sound()
# d1.sound()

# 4. Write a Python program to demonstrate method overriding using Login and AdminLogin classes.

# class Login:
#     def access(self):
#         print("User login access")

# class AdminLogin(Login):
#     def access(self):
#         print("Admin login access")

# l1 = Login()
# a1 = AdminLogin()

# l1.access()
# a1.access()

# 5. Write a Python program to demonstrate polymorphism using the same result() method in SchoolStudent and CollegeStudent classes.

# class SchoolStudent:
#     def result(self):
#         print("School student result")

# class CollegeStudent:
#     def result(self):
#         print("College student result")

# s1 = SchoolStudent()
# c1 = CollegeStudent()

# s1.result()
# c1.result()

# 6. Write a Python program to demonstrate polymorphism by passing different objects to the same function to perform their respective operations.

class Addition:
    def operation(self, a, b):
        print("Addition =", a + b)

class Multiplication:
    def operation(self, a, b):
        print("Multiplication =", a * b)

def calculate(obj, a, b):
    obj.operation(a, b)

calculate(Addition(), 10, 20)
calculate(Multiplication(), 10, 20)