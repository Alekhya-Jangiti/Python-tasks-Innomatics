
# 1. Create a Student class using a constructor to initialize and display student details.

# class Student:
#     def __init__(self, name, branch, year):
#         self.name = name
#         self.branch = branch
#         self.year = year

#     def display(self):
#         print("Name :", self.name)
#         print("Branch :", self.branch)
#         print("Year :", self.year)

# s1 = Student("Smiley", "CSE", "Third Year")
# s1.display()

# 2. Create a class to calculate the total and average marks of a student in three subjects.

# class Student:
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def calculate(self):
#         total = self.m1 + self.m2 + self.m3
#         average = total / 3
#         print("Total =", total)
#         print("Average =", average)

# s1 = Student(80, 75, 90)
# s1.calculate()

# 3. Create a class with a constructor that assigns a default value when no value is provided.

# class Employee:
#     def __init__(self, name, department="IT"):
#         self.name = name
#         self.department = department

#     def display(self):
#         print("Name :", self.name)
#         print("Department :", self.department)

# e1 = Employee("Meghana")
# e1.display()

# 4. Create a class using a constructor to initialize cost price and selling price and return the profit percentage.

# class Sales:
#     def __init__(self, cost, selling):
#         self.cost = cost
#         self.selling = selling

#     def profit_percentage(self):
#         profit = self.selling - self.cost
#         return (profit / self.cost) * 100

# s = Sales(5000, 6000)
# print("Profit Percentage =", s.profit_percentage())

# 5. Create a Python class CricketMatch to store and display details of multiple cricket matches, including tournament, venue, teams, overs, and winner, using a constructor.

# class CricketMatch:
#     tournament = "IPL"   
#     venue = "Hyderabad" 
#     def __init__(self, team1, team2, overs, winner):
#         self.myTeam1 = team1
#         self.myTeam2 = team2
#         self.myOvers = overs
#         self.myWinner = winner

#     def displayDetails(self):
#         print(f" Tournament : {CricketMatch.tournament}")
#         print(f" Venue : {CricketMatch.venue}")
#         print(f" Team 1 : {self.myTeam1}")
#         print(f" Team 2 : {self.myTeam2}")
#         print(f" Overs : {self.myOvers}")
#         print(f" Winner : {self.myWinner}")

# m1 = CricketMatch("RCB", "MI", 20, "RCB")
# print("----------------match 1---------------")
# m1.displayDetails()
# m2 = CricketMatch("CSK", "SRH", 20, "SRH")
# print("----------------match 2---------------")
# m2.displayDetails()
# m3 = CricketMatch("KKR", "DC", 20, "KKR")
# print("----------------match 3---------------")
# m3.displayDetails()

# 6. Create a Python class Employee to store and display details of multiple employees, including their name, age, salary, department, company name, and company location, using a constructor.

class Employee:
    company_name = "TCS"   
    company_location = "Hyderabad"  

    def __init__(self, name, age, salary, department):
        self.myName = name
        self.myAge = age
        self.mySalary = salary
        self.myDepartment = department

    def displayDetails(self):
        print(f" Name : {self.myName}")
        print(f" Age : {self.myAge}")
        print(f" Salary : {self.mySalary}")
        print(f" Department : {self.myDepartment}")
        print(f" Company : {Employee.company_name}")
        print(f" Location : {Employee.company_location}")
e1 = Employee("Rahul", 25, 40000, "IT")
print("----------------employee 1---------------")
e1.displayDetails()
e2 = Employee("Priya", 24, 85000, "HR")
print("----------------employee 2---------------")
e2.displayDetails()
e3 = Employee("Kiran", 26, 50000, "Finance")
print("----------------employee 3---------------")
e3.displayDetails()
