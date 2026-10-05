# 1. Create an instance method to display college details. (without input and without return)
class College:
    def details(self):
        print("College :JNTUH College of Engineering Sultanpur")
        print("Branch :Computer Science Engineering")
c=College()
c.details()
#-------------------------------------------------------------------------------------------------------------
# 2. To check whether a number is even or odd. (with input and without return)
class Number:
    def check(self, n):
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
n1 = Number()
n1.check(20)
#-------------------------------------------------------------------------------------------------------------

# 3. return the number of months in a year. (without input and with return)
class Months:
    def get_months(self):
        return 12
m = Months()
months = m.get_months()
print("Months in a year:", months)
#-------------------------------------------------------------------------------------------------------------

# 4. Take a number and returns its last digit. (with input and with return)
class Number:
    def last_digit(self,n):
        return n%10
n1=Number()
res=n1.last_digit(486328)
print("Last digit of given number = ",res)
#-------------------------------------------------------------------------------------------------------------

# create a Bank class demonstrating all four types of instance methods
class Bank:
    # 1. Without input and Without return
    def welcome(self):
        print("Welcome to ABC Bank")

    # 2. With input and Without return
    def check_balance(self, balance):
        if balance >= 1000:
            print("Sufficient Balance")
        else:
            print("Low Balance")

    # 3. Without input and With return
    def bank_name(self):
        return "ABC Bank"

    # 4. With input and With return
    def calculate_interest(self, amount):
        return amount * 3 / 100

b1 = Bank()
b1.welcome()
b1.check_balance(5000)
name = b1.bank_name()
print("Bank Name:", name)
interest = b1.calculate_interest(10000)
print("Interest:", interest)
