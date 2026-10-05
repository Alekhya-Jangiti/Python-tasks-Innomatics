# if True:
#     print("If block executed")
# print("program ended")

#check whether it is equal to 10
# n=int(input("Enter number :"))
# if n==10:
#     print("Number=10")

#which gaves 15% discount if the price is greater than 5000 in total bill.
# bp=int(input("Enter number :"))
# if bp> 5000:
#     discount=(15/100)*bp
#     total_bill=bp-discount
#     print("Billing price before discount:",bp)
#     print("Billing price after discount:",total_bill)

#if-else

# if True:
#     print("If block executed")
# else:
#     print("else block executed")

#to check given number is 10
# n=int(input("Enter num :"))
# if n==10:
#     print("This is 10")
# else:
#     print("this is not 10")

# check given number is +ve or not
# n=int(input("Enter num :"))
# if n>0:
#     print("Number is positive")
# else:
#     print("Number is negative")

# check the biggest number among 2 values
# n1=int(input("Enter num 1:"))
# n2=int(input("Enter num 2:"))
# if(n1>n2):
#     print(n1,"is greater than",n2)
# else:
#     print(n2,"is greater than",n1)

# check number is even or not
# n=int(input("Enter num :"))
# if n%2==0:
#     print(n, " is even number")
# else:
#     print(n, " is odd number")

#program to check given value is vowel or not
# n=input("Enter an alphabet :")
# if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
#     print(n," is an vowel")
# else:
#     print(n,"value is consonent")

#given value is alphabet or not
# ch=input("Enter value :")
# if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
#     print("it is an alphabet")
# else:
#     print("Not an alphabet")

#given value is digit or not
# ch=input("Enter value :")
# if (ch>="0" and ch<="9"):
#     print("it is a digit")
# else:
#     print("Not a digit")

#program that name="hero" and password=Hero@123 then it show login succesful if not invalid credentials
# name=input("Enter name :")
# password=input("Enter password :")
# if name=="Hero" and password=="Hero@123":
#     print("Login successful")
# else:
#     print("Invalid credentials")
    
#falsy
# if():
#     print("condition True : if block executes")
# else:
#     print("condition false : else block executes")

#if elif else
# if(False):
#     print("condition 1 : If block")
# elif(False):
#     print("condition 1 is false: elif block")
# elif(""):
#     print("condition 1 & 2 is false and cond3 True : 2nd elif block")
# else:
#     print("all above false : else block")

#check number is +ve or _ve or 0
# n=int(input("Enter num :"))
# if(n>0):
#     print("positive number")
# elif(n<0):
#     print("negative number")
# else:
#     print("zero")

# check given character is alphabet r digit or symbol
# ch=input("Enter character :")
# if((ch>='a'and ch<='z') or (ch>='A' and ch<='Z')):
#     print("Alphabet")
# elif(ch>="0" and ch<="9"):
#     print("Digit")
# else:
#     print("symbol")

#display the grade based on given marks
# m=int(input("Enter marks :"))
# if(m>90):
#     print("O")
# elif(m<=90 and m>70):
#     print("A")
# elif(m<=70 and m>50):
#     print("B")
# elif(m<=50 and m>=35):
#     print("C")
# else:
#     print("Fail")

#nested if
# if(True):
#     print("Outer if ")
#     if(True):
#         print("Inner if")
#     else:
#         print("Inner else")
# else:
#     print("outer else")
    
#check even or odd only if it is +ve
# n=int(input("Enter num :"))
# if(n>0):
#     print("positive num")
#     if(n%2==0):
#         print("even")
#     else:
#         print("odd")
# else:
#     print("negative num")

#display smallest num from given 2 values only if they are not equal

# n1=int(input("Enter num1 :"))
# n2=int(input("Enter num2 :"))
# if(n1!=n2):
#     if(n1<n2):
#         print("n1 is smaller than n2")
#     else:
#         print("n2 is smaller than n1")
# else:
#     print("Both numbers equal")

#match case
# ch=int(input("Enter character :"))
# match ch:
#     case 1:
#         print("case 1 executed")
#     case 2:
#         print("case 2 executed")
#     case 3:
#         print("case 3 executed")
#     case _:
#         print("default case executed")

#traffic light
# color=input("Enter color :")
# match color:
#     case "red":
#         print("Vehicle should stop")
#     case "yellow":
#         print("Vehicle should ready to go")
#     case "green":
#         print("Vehicle should go")
#     case _:
#         print("Default case")

#shapes
# side=int(input("enter number of sides :"))
# match side:
#     case 3:
#         print("traingle")
#     case 4:
#         print("rectangle")
#     case 5:
#         print("pentagon")
#     case 6:
#         print("hexagon")
#     case 7:
#         print("heptagon")
#     case 8:
#         print("octagon")
#     case _:
#         print("enter valid number of sides")

#days
# days=int(input("Enter a day :"))
# match days:
#     case 1:
#         print("Monday")
#     case 2:
#         print("tuesady")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("enter valid day")

#operators
# n1=int(input("enter num1 :"))
# n2=int(input("enter num2 :"))
# operator=input("Enter operator :")
# match operator:
#     case "+":
#         print("sum=",n1+n2)
#     case "-":
#         print("sub=",n1-n2)
#     case "*":
#         print("mul=",n1*n2)
#     case "/":
#         print("div=",n1/n2)
#     case _:
#         print("invalid operator")

#menu driven program
print("Enter 2 numbers")
n1=int(input("enter num1 :"))
n2=int(input("enter num2 :"))
print("select an option from the given choices :")
print("1. Add\n 2.Sub\n 3.Div\n 4.Mul\n 5.Remainder")
opt=int(input("Your Option :"))
match opt:
    case 1:
        print("Sum=",n1+n2)
    case 2:
        print("Sub=",n1-n2)
    case 3:
            print("Div=",n1/n2)
    case 4:
        print("Mul=",n1*n2)
    case 5:
            print("Remainder=",n1%n2)
    case _:
            print("enter valid option")