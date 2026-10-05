# 1. Print all prime numbers in a given range

# print("Prime numbers in given range are :")
# for j in range(1,100,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         print(n,end=" ")

# 2. Print all Armstrong numbers in a given range

# print("Armstrong numbers in given range are :")
# for j in range(1,1000,1):
#     n=j
#     temp=n
#     sum=0
#     for i in range(1,n+1,1):
#         ld=n%10
#         sum=sum+ld**3
#         n=n//10
#     if temp==sum:
#         print(temp,end=" ")

# 3. Print all perfect numbers in a given range

# for j in range(1,1000,1):
#     n=j
#     sum=0
#     for i in range(1,n,1):
#         if n%i==0:
#             sum+=i
#     if sum==n:
#         print(sum,end=" ")

# 4. Print all factors of every number from 1 to N

# for j in range(1,16,1):
#     print(f"Factors of {j} :",end=" ")
#     n=j
#     for i in range(1,n+1,1):
#         if n%i==0:
#             print(i,end=" ")
#     print()

# 5. Print all numbers in a given range whose digit sum is exactly 10.

# print("Numbers whose digit sum is 10 are :")
# for j in range(1,100,1):
#     n=j
#     sum=0
#     for i in range(1,n+1,1):
#         r=n%10
#         n=n//10
#         sum=sum+r
#     if(sum==10):
#         print(i,end="  ")

# 6. Print all numbers in a given range that have exactly 3 factors

for j in range(1,50,1):
    n=j
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count+=1
    if count==3:
        print(i,end=" ")