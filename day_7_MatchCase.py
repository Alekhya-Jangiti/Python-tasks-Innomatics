# 1. Print the day of the week using match-case

# option=int(input("Enter a Number :"))
# match option:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Sorry... Invalid day")

# 2. Check whether a character is a vowel or consonant

# ch=input("Enter a Character :")
# match ch:
#     case "a" | "e" | "i" | "o" | "u":
#         print("Vowel")
#     case "A" | "E" | "I" | "O" | "U":
#         print("Vowel")
#     case _:
#         print("Consonent")

# 3. Create a menu-driven area calculator

# print("1. Circle\n2. Rectangle\n3. Square\n4. Triangle")
# choice=int(input("Enter your choice :"))
# match choice:
#     case 1:
#         r = float(input("Enter radius: "))
#         print("Area of circle =", 3.14 * r * r)
#     case 2:
#         l = float(input("Enter length: "))
#         b = float(input("Enter breadth: "))
#         print("Area of rectangle =", l * b)
#     case 3:
#         s = float(input("Enter side: "))
#         print("Area of square =", s * s)
#     case 4:
#         b = float(input("Enter base: "))
#         h = float(input("Enter height: "))
#         print("Area of triangle =", 0.5 * b * h)
#     case _:
#         print("Invalid choice")

# 4. Create a movie ticket booking program

# print("1. Regular - ₹150\n2. Premium - ₹250\n3. Recliner - ₹400")
# choice = int(input("Enter your choice: "))
# tickets = int(input("Enter number of tickets: "))
# match choice:
#     case 1:
#         price = 150
#         print("Seat Type: Regular")
#         print("Total Amount =", price * tickets)
#     case 2:
#         price = 250
#         print("Seat Type: Premium")
#         print("Total Amount =", price * tickets)
#     case 3:
#         price = 400
#         print("Seat Type: Recliner")
#         print("Total Amount =", price * tickets)
#     case _:
#         print("Invalid choice")

# 5. Create an ATM program
# print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
# choice = int(input("Enter your choice: "))
# balance=10000
# match choice:
#     case 1:
#         print("Available Balance =", balance)
#     case 2:
#         amount = float(input("Enter deposit amount: "))
#         balance = balance + amount
#         print("Amount Deposited Successfully")
#         print("Updated Balance =", balance)
#     case 3:
#         amount = float(input("Enter withdrawal amount: "))
#         if amount <= balance:
#             balance = balance - amount
#             print("Please collect your cash")
#             print("Remaining Balance =", balance)
#         else:
#             print("Insufficient Balance")
#     case 4:
#         print("Thank you for using ATM")
#     case _:
#         print("Invalid choice")

# 6. Take a package status code and display the current delivery status.

print("1. Order Placed\n2. Packed\n3. Shipped\n4. Out of Delivery\n5. Delivered")
choice = int(input("Enter status : "))
match choice:
    case 1:
        print("Your order has been placed.")
    case 2:
        print("Your order has been packed.")
    case 3:
        print("Your order has been shipped.")
    case 4:
        print("Your order is out for delivery.")
    case 5:
        print("Your order has been delivered.")
    case _:
        print("Invalid status")
