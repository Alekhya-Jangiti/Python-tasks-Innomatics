
# 1. An application maintains a bank balance as a global variable. Write a Python function that accepts a deposit amount and updates the balance.

# balance = 5000
# def deposit():
#     global balance
#     amount = 2000
#     balance += amount
#     print("Balance =", balance)
# deposit()

# 2. Write a Python program to demonstrate the difference between modifying a local variable and modifying a global variable with the same name.

# count = 10
# def first():
#     count = 20
#     print("Inside first =" ,count)
# def second():
#     global count
#     count = 30
#     print("Inside second =" ,count)
    
# first()
# print("After first =" ,count)
# second()
# print("After second =", count)

# 3. Create a nested-function program for an employee management scenario where the employee's department is defined in the outer function and accessed by the inner function.

# def employee():
#     department = "Software development"
#     def details():
#         print(department)
#     details()
# employee()

# 4. Create a counter using nested functions where the counter value is maintained by the outer function. The inner function should update the same counter every time it is called.

# def counter():
#     count = 0
#     def increase():
#         nonlocal count
#         count += 1
#         print(count)
#     increase()
#     increase()
#     increase()
# counter()

# 5. Write a Python program to process five given numbers and determine their highest value, lowest value, and total. Use appropriate built-in functions and display the results.

# def calculate(a,b,c,d,e):
#     maximum = max(a,b,c,d,e)
#     minimum = min(a,b,c,d,e)
#     total = a + b + c + d + e
#     return maximum, minimum, total
# def display(maximum,minimum,total):
#     print("Maximum =" ,maximum)
#     print("Minimum =" ,minimum)
#     print("Total =" ,total)
    
# maximum, minimum, total = calculate(25,10,15,40,20)
# display(maximum, minimum, total)

# 6. Write a Python program to demonstrate how Python resolves a variable when the same variable name is defined in local, enclosing, and global scopes. Use nested functions and display the value accessed from the inner function.

x = "Global"
def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print("Value =", x)
    inner()
outer()

