# 1. Count the number of digits in a number.

# n=int(input("Enter a Number :"))
# temp=n
# count=0
# while(n>0):
#     n=n//10
#     count+=1
# print(f"Number of Digits in given Number {temp} are {count}")

# 2. Find the sum of digits of a number.

# n=int(input("Enter a number :"))
# temp=n
# sum=0
# for i in range(1,n+1,1):
#     r=n%10
#     sum=sum+r
#     n=n//10
# print(f"Sum of Digits in given number {temp} is {sum}")

# 3. Find largest digit in a given number :

# n=int(input("Enter a Number :"))
# largest=0
# while n!=0:
#     r=n%10
#     if(r>largest):
#         largest=r
#     n=n//10
# print(f"Largest Number is {largest}")

# 4. Check whether a number is a palindrome.

# n=int(input("Enter a Number :"))
# rev=0
# temp=n
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if(temp==rev):
#     print(f"{temp} is Palindrome")
# else:
#     print(f"{temp} is Not a Palindrome")

# 5. Count even and odd digits in a number

# n=int(input("Enter a Number :"))
# count=0
# res=0
# while n>0:
#     r=n%10
#     if n%2==0:
#         count+=1
#     else:
#         res+=1
#     n=n//10
# print(f"Even Digits : {count}")
# print(f"Odd Digits : {res}")

# 6. Remove all zeros from a number

n=int(input("Enter a Number :"))
res=0
place=1
while n>0:
    r=n%10
    if r!=0:
        res=res+r*place
        place=place*10
    n=n//10
print(f"Number after removing zeroes : {res}")
