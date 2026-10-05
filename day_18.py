
# 1. Create a class with a destructor that displays a message

# class Demo:
#     def __init__(self, name):
#         self.name = name
#         print("Object created")

#     def __del__(self):
#         print("Object deleted")
# d1 = Demo("Python")
# del d1

# 2. Create an Employee class and demonstrate when the constructor and destructor are invoked.

# class Employee:
#     def __init__(self):
#         print("Employee object is created")

#     def __del__(self):
#         print("Employee object is deleted")
# e1 = Employee()
# print("Employee details are processed")
# del e1
# print("Program Ended")

# 3. Create a Login class to demonstrate destructor.

# class Login:
#     def __init__(self):
#         print("Login object is created")

#     def __del__(self):
#         print("Login object is destroyed")
# l1 = Login()
# print("User is logged in")
# del l1
# print("Program Ended")

# 4. Create a Student class with a method to display student information. Create an EngineeringStudent class that inherits from Student.

# class Student:
#     def display_student(self):
#         print("Student information")
        
# class EngineeringStudent(Student):
#     def display_branch(self):
#         print("Computer Science")
        
# s1 = EngineeringStudent()
# s1.display_student()
# s1.display_branch()

# 5. Create a Vehicle class with methods to start and stop a vehicle. Create a Car class that inherits these methods.

# class Vehicle:
#     def start(self):
#         print("Vehicle started")

#     def stop(self):
#         print("Vehicle stopped")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")
# c1 = Car()
# c1.start()
# c1.drive()
# c1.stop()

# 6. Create a TrafficLight class with a method to display the traffic signal. Create a RoadSignal class that inherits from TrafficLight.

class TrafficLight:
    def signal(self):
        print("Traffic Light: Red")

class RoadSignal(TrafficLight):
    def action(self):
        print("Action: Stop")

r1 = RoadSignal()
r1.signal()
r1.action()