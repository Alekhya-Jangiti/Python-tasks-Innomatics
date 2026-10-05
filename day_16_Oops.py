
# 1. Write a Python program using a Calculator class and a static method to calculate the square of a given number.

# class Calculator:
#     @staticmethod
#     def square(n):
#         return n * n
# print(Calculator.square(8))

# 2. Write a Python program using a Bank class and a static method to calculate simple interest.

# class Bank:
#     @staticmethod
#     def simple_interest(p,t,r):
#         return ((p*t*r)/100)
# SI=Bank.simple_interest(10000,2,5)
# print("Simple Interest = ",SI)

# 3. Create a Python class EmployeeDetails to store and display employee information.

# class EmployeeDetails:
#     def assignDetails(self, name, department, salary):
#         self.myName = name
#         self.myDepartment = department
#         self.mySalary = salary
        
#     def displayDetails(self):
#         print(f" Name : {self.myName}")
#         print(f" Department : {self.myDepartment}")
#         print(f" Salary : {self.mySalary}")

# e1 = EmployeeDetails()
# e1.assignDetails("Rahul", "IT", 35000)
# print("---------------- Employee 1 ----------------")
# e1.displayDetails()

# e2 = EmployeeDetails()
# e2.assignDetails("Priya", "HR", 40000)
# print("---------------- Employee 2 ----------------")
# e2.displayDetails()

# 4. Create a ProductDetails class using a class method to assign and display details of multiple products.

# class ProductDetails:
#     store_name = "Amazon"

#     @classmethod
#     def displayDetails(cls, name, price, category):
#         print("Name :", name)
#         print("Price :", price)
#         print("Category :", category)
#         print("Store :", cls.store_name)

# print("---------------- Product 1 ----------------")
# ProductDetails.displayDetails("Laptop", 55000, "Electronics")

# print("---------------- Product 2 ----------------")
# ProductDetails.displayDetails("Shoes", 2500, "Footwear")

# print("---------------- Product 3 ----------------")

# ProductDetails.displayDetails("Watch", 3500, "Accessories")


# 5. Create a class StudentDetails to manage student and college information.

# class StudentDetails:
#     college_name = "JNTUH"
#     @staticmethod
#     def displayCollege():
#         print(f" College Name : {StudentDetails.college_name}")
        
#     def assignDetails(self, name, branch, year):
#         self.myName = name
#         self.myBranch = branch
#         self.myYear = year
#     def displayDetails(self):
#         print(f" Name : {self.myName}")
#         print(f" Branch : {self.myBranch}")
#         print(f" Year : {self.myYear}")
#         print(f" College : {StudentDetails.college_name}")
# StudentDetails.displayCollege()

# s1 = StudentDetails()
# s1.assignDetails("Sweety", "CSE", "Final Year")
# print("---------------- Student 1 ----------------")
# s1.displayDetails()

# s2 = StudentDetails()
# s2.assignDetails("Preethi", "ECE", "Third Year")
# print("---------------- Student 2 ----------------")
# s2.displayDetails()

# 6. Create a Python class IPLPlayerDetails to store and display IPL player information.

class IPLPlayerDetails:
    tournament_name = "IPL"

    def assignDetails(self, name, team, role):
        self.myName = name
        self.myTeam = team
        self.myRole = role

    def displayDetails(self):
        print(f" Player : {self.myName}")
        print(f" Team : {self.myTeam}")
        print(f" Role : {self.myRole}")
        print(f" Tournament : {IPLPlayerDetails.tournament_name}")
p1 = IPLPlayerDetails()
p1.assignDetails("Virat Kohli", "RCB", "Batsman")
print("---------------- Player 1 ----------------")
p1.displayDetails()

p2 = IPLPlayerDetails()
p2.assignDetails("Jasprit Bumrah", "MI", "Bowler")
print("---------------- Player 2 ----------------")
p2.displayDetails()

p3 = IPLPlayerDetails()
p3.assignDetails("Ruturaj Gaikwad", "CSK", "Batsman")
print("---------------- Player 3 ----------------")
p3.displayDetails()


