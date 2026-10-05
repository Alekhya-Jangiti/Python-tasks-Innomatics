# 1. display company details (without input and without return)
class Company:
    @staticmethod
    def details():
        print("Company : ABC Technologies")
        print("Location : Hyderabad")
        print("Department : IT")
Company.details()
#-------------------------------------------------------------------------------------------------------------

# 2.Display a multiplication table (without input and without return)
class Table:
    @staticmethod
    def multiplication():
        for i in range(1, 11):
            print(5, "*", i, "=", 5 * i)
Table.multiplication()
#-------------------------------------------------------------------------------------------------------------

# 3. Check whether a year is a leap year (with input and without return)
class Year:
    @staticmethod
    def leap_year(year):
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
Year.leap_year(2024)
#-------------------------------------------------------------------------------------------------------------

# 4. Check whether a person is eligible to vote (with input and without return)
class Voter:
    @staticmethod
    def check_age(age):
        if age>=18:
            print("Eligible for Vote")
        else:
            print("Not Eligible for Vote")
Voter.check_age(20)
#-------------------------------------------------------------------------------------------------------------

# 5. Return the number of days in a week (without input and with return)
class Week:
    @staticmethod
    def get_days():
        return 7
days=Week.get_days()
print("Days in a week :",days)
#-------------------------------------------------------------------------------------------------------------

# 6. Return the current course (without input and with return)
class Course:
    @staticmethod
    def get_course():
        return "Python Full Stack"
course = Course.get_course()
print(course)
#-------------------------------------------------------------------------------------------------------------

# 7. Calculate simple interest (with input and with return)
class Bank:
    @staticmethod
    def simple_interest(p,t,r):
        return ((p*t*r)/100)
SI=Bank.simple_interest(10000,2,5)
print("Simple Interest = ",SI)
#-------------------------------------------------------------------------------------------------------------

# 8. Find area of rectangle (with input and with return)
class Rectangle:
    @staticmethod
    def area(length, breadth):
        return length * breadth
result = Rectangle.area(10, 5)
print("Area =", result)
#-------------------------------------------------------------------------------------------------------------

class Employee:
    # 1. Without input and Without return
    @staticmethod
    def company_message():
        print("Welcome to ABC Technologies")
        
    # 2. With input and Without return
    @staticmethod
    def check_experience(years):
        if years >= 2:
            print("Experienced Employee")
        else:
            print("Fresher")

    # 3. Without input and With return
    @staticmethod
    def get_department():
        return "Software Development"

    # 4. With input and With return
    @staticmethod
    def calculate_bonus(salary):
        return salary * 10 / 100

Employee.company_message()
Employee.check_experience(1)
department = Employee.get_department()
print("Department:", department)
bonus = Employee.calculate_bonus(30000)
print("Bonus:", bonus)