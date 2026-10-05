# def sayHello():
#     print("Hello")
# sayHello()
# sayHello()

#--------------------------named function without input and without return-----------
# def printHelloWorld():
#     print("Hello World")
# printHelloWorld()

#add numbers
# def addTwo():
#     a=10
#     b=20
#     print (a+b)
# addTwo()

# write code to display smallest number from three numbers
# def smallNum():
#     a=10
#     b=60
#     c=54
#     if(a<b and a<c):
#         print(f"{a} is small")
#     elif(b<c and b<a):
#         print(f"{b} is small")
#     else:
#         print(f"{c} is small")
# smallNum()

#------------------------------named function with input and without return type-----------------------
# def displayName(name):
#     name="Hero"
#     print(name)
# displayName("Hero")

# to check given number is even or odd
# def evenOdd(n):
#     if(n%2==0):
#         print(f"{n} is Even")
#     else:
#         print(f"{n} is Odd")
# evenOdd(23)
# evenOdd(6)
# evenOdd(100)

# to display average of three numbers
# def avgOfThree(n1,n2,n3):
#     avg=(n1+n2+n3)/3
#     print(f"Average of {n1},{n2},{n3} is {avg}")
# avgOfThree(23,78,43)

#------------------------named function without input and with return---------------------
# def displayName():
#     name="Hero"
#     return name
# res=displayName()
# print(res)

# factorial of num
# def factorialEx():
#     n=6
#     fact=1
#     for i in range(n,0,-1):
#         fact=fact*i
#     return fact
# # res=factorialEx()
# # print(res)
# print(factorialEx())

#return sum of even numbers in range 1 to 10
# def sumEvenNum():
#     sum=0
#     for i in range(1,11,1):
#         sum=sum+i
#     return sum
# print(sumEvenNum())

#------------------------named function without input and with return---------------------
# def displayName(myName):
#     return myName
# name=displayName("Anku")
# print(f"My name is {name}")

#check prime number
# def checkPrime(n):
#     count=0
#     for i in range(1,n+1,1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return n
#     else:
#         pass
# res=checkPrime(23)
# print(f"{res} is Prime Number")

#----------------------------------------Lambda Function-----------------------------------------

# lambda function without input(Argument) and with return
# x=lambda : print("Hello World")
# x()

# x=lambda : print("Hello World")
# print(x()) #None

# lambda function with input(Argument) and without return
# displayName=lambda fname: print(f"My name is {fname}")
# displayName("Alekya")

# lambda function without input(Argument) and with return
# displayMsg=lambda:"Hello World"
# print(displayMsg())

# lambda function with input(Argument) and with return
# displayName=lambda fname:"My name is"+fname
# print(displayName("Alekhya"))

#Add two numbers using lambda function
# addTwo=lambda n1,n2 : f"Sum of two numbers is {n1+n2}"
# print(addTwo(20,30))
    
# -----------------------------------Lambda Function-Conditional Statements----------------------------------------
#syntax :  lambda : true-value if condition else false-value

# checkEven= lambda :"Even" if 11%2==0 else "Odd"
# print(checkEven())

# lambds function with input and with return
# checkEven= lambda n: "Even" if n%2==0 else "Odd"
# print(checkEven(15))