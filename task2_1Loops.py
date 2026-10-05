# # 1.Find the average of numbers from 1 to N.
# n=int(input("Enter number :"))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i
# avg=sum/n
# print("Average of numbers :",avg)

# # 2.Find the sum of squares of numbers from 1 to N.
# n=int(input("Enter Number :"))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+(i*i)
# print("Sum of squares :",sum)

# # 3.Find the sum of cubes of numbers from 1 to N.
# n=int(input("Enter Number :"))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+(i**3)
# print("Sum of cubes :",sum)

# # 4.Calculate the power of a number without using the ** operator.
# b=int(input("Enter base :"))
# p=int(input("Enter power :"))
# res=1
# for i in range(p):
#     res=res*b
# print(res)

# # 5.Display the first N terms of the Fibonacci series.
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

# # 6.Display the first N terms of the series:
# n=int(input("Enter number :"))
# for i in range(1,n+1,1):
#     if i==1:
#         print("1",end=" ")
#     else:
#         print(f"1/{i}",end=" ")

# # 7.Display the first N terms of the series:
# n=int(input("Enter number :"))
# num=0
# for i in range(1,n+1,1):
#     num=num*10+1
#     print(num,end=" ")

# # 8.Display the first N terms of the series:
# n=int(input("Enter number :"))
# res=1
# for i in range(1,n+1,1):
#     if(i==1):
#         print(1,end=" ")
#     else:
#         res=res*3
#         print(res,end=" ")
        
# even numbers one side odd numbers one side middle zeroes

# n=59026830
# even=0
# odd=0
# zero = 0
# while n >0:
#     digit= n % 10
#     if digit ==0:
#         zero+=1
#     elif digit % 2==0:
#         even = even * 10 +digit
#     else:
#         odd = odd * 10 +digit
#     n= n //10
# res = even
# while zero > 0:
#     res = res * 10
#     zero -= 1
# print(f"{res}{odd}")

# arrange digits in a way that greater to smaller

n=4981231
ans=0
for i in range(9,-1,-1):
    temp=n
    while temp > 0:
        digit = temp % 10
        if digit == i:
            ans = (ans * 10) + digit
        temp = temp // 10
print(ans,end="")
        
        