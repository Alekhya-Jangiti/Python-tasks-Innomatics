# 1st Example Bank

class Bank:
    bank_name = "SBI"
    branch = "Hyderebad"
    def __init__(self,name,age,acc_number,balance):
        self.name = name
        self.age = age
        self.acc_number = acc_number
        self.balance = balance
        
    def displayDetails(self):
        print("Bank Name :",Bank.bank_name)
        print("Branch :",Bank.branch)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Account Number :",self.acc_number)
        print("Balance :",self.balance)
        
b1=Bank("Alekhya",22,1011,50000)
print("-----------------Customer-1---------------------")
b1.displayDetails()
b2=Bank("Rishi", 21,1020,20000)
print("-----------------Customer-2---------------------")
b2.displayDetails()
b3=Bank("Sweety",20,1112,10500)
print("-----------------Customer-3---------------------")
b3.displayDetails()
#-----------------------------------------------------------------------------------------------------------------
# Example Cricket Match

class CricketMatch:
    tournament = "IPL"   
    venue = "Hyderabad" 
    def __init__(self, team1, team2, overs, winner):
        self.myTeam1 = team1
        self.myTeam2 = team2
        self.myOvers = overs
        self.myWinner = winner

    def displayDetails(self):
        print(f" Tournament : {CricketMatch.tournament}")
        print(f" Venue : {CricketMatch.venue}")
        print(f" Team 1 : {self.myTeam1}")
        print(f" Team 2 : {self.myTeam2}")
        print(f" Overs : {self.myOvers}")
        print(f" Winner : {self.myWinner}")

m1 = CricketMatch("RCB", "MI", 20, "RCB")
print("----------------match 1---------------")
m1.displayDetails()
m2 = CricketMatch("CSK", "SRH", 20, "SRH")
print("----------------match 2---------------")
m2.displayDetails()
m3 = CricketMatch("KKR", "DC", 20, "KKR")
print("----------------match 3---------------")
m3.displayDetails()
#-----------------------------------------------------------------------------------------------------------------

# Example Employee

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
