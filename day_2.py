# 1. Find all factors of a number.

# n=int(input("Enter a number :"))
# print(f"factors of {n} is :",end=" ")
# for i in range(1,n,1):
#     if(n%i==0):
#         print(i,end=" ")

# 2. Find the factorial of a number.

# n=int(input("Enter a Number :"))
# fact=1
# for i in range(1,n+1,1):
#     fact=fact*i
# print(f"Factorial of {n} is {fact}")

# 3.Find the sum of squares of numbers from 1 to N.

# n=int(input("Enter Number :"))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+(i*i)
# print("Sum of squares :",sum)

# 4. Print the multiplication table of a number.

# n=int(input("Enter a Number :"))
# print("Multiplication Table of",n ,"is :")
# for i in range(1,11,1):
#     print(f"{n} x {i} = {n*i}")

# 5.Display the first N terms of the Fibonacci series.

# n=int(input("Enter a number :"))
# print("Fibanacci Series :")
# a=0
# b=1
# print(a,end=" ")
# print(b,end=" ")
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")

# 6. Check whether a number is prime or not

n=int(input("Enter a Number :"))
count=0
for i in range(1,n+1,1):
    if n%i==0:
        count+=1
if count==2:
    print(f"{n} is Prime Number")
else:
    print(f"{n} is Not a Prime Number")
    


