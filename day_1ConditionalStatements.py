
# 1. Find the largest of three numbers.
# n1=int(input("Enter Number 1:"))
# n2=int(input("Enter Number 2:"))
# n3=int(input("Enter Number 3:"))
# if (n1> n2 and n3):
#     print(f"{n1} is largest")
# elif (n2> n1 and n3):
#     print(f"{n2} is largest")
# else:
#     print(f"{n3} is largest")

# 2.Check whether a given year is a Leap Year or not.
# year=int(input("Enter Year :"))
# if(year%400==0):
#     print(f"{year} is a Leap year")
# elif(year%4==0 or year%100==0):
#     print(f"{year} is a Leap year")
# else:
#     print(f"{year} is not a Leap year")

# # 3.Check the type of triangle based on its sides.

# s1=int(input("Enter side1 of triangle :"))
# s2=int(input("Enter side2 of triangle :"))
# s3=int(input("Enter side3 of triangle :"))
# if(s1==s2 and s2==s3):
#     print("Equalient Triangle")
# elif(s1==s2 or s2==s3 or s1==s3):
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

# # 4.Calculate the electricity bill based on units consumed.

# units=int(input("Enter number of units consumed :"))
# if(units>=0 and units<=100):
#     print("₹2/unit")
# elif(units>=101 and units<=200):
#     print("₹3/unit")
# elif(units>=201 and units<=300):
#     print("₹5/unit")
# else:
#     print("₹7/unit")
    
#  5.Display the grade based on average only if the student has passed in all 4 subjects.

# py=int(input("Enter python marks :"))
# m=int(input("Enter maths marks :"))
# e=int(input("Enter english marks :"))
# sql=int(input("Enter sql marks :"))
# avg=(py+m+e+sql)/4
# print(f"Average: {avg}")
# if(py>=35 and m>=35 and e>=35 and sql>=35):
#     if(avg>=90):
#         print("O")
#     elif(avg>=80):
#         print("A")
#     elif(avg>=70):
#         print("B")
#     elif(avg>=60):
#         print("C")
#     elif(avg>=50):
#         print("D")
#     else:
#         print("E")
# else:
#     print("Failed")

#  6.Program to create a simple calculator

n1=int(input("Enter num 1 :"))
n2=int(input("Enter num 2 :"))
operator=input("Enter Operator (+, -, *, /, //, %) :")
if operator == "+" :
    print(f"Addition of {n1} and {n2} is {n1+n2}")
elif operator == "-" :
    print(f"Substraction of {n1} and {n2} is {n1-n2}")
elif operator == "*" :
    print(f"Multiplication of {n1} and {n2} is {n1*n2}")

elif operator == "/" :
    print(f"Divison of {n1} and {n2} is {n1/n2}")

elif operator == "//" :
    print(f"Floor Divison of {n1} and {n2} is {n1//n2}")
elif operator == "%" :
    print(f"Modulus of {n1} and {n2} is {n1%n2}")
else:
    print("Invalid Operator")


