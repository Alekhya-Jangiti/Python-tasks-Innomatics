
# 1. Print numbers from 1 to 10 and stop when the number is 6.

# for i in range(1,11,1):
#     if i==6:
#         break
#     print(i)

# 2. Print numbers from 1 to 100 and stop when the first number divisible by both 3 and 5 is found.

# for i in range(1,101,1):
#     if i%3==0 and i%7==0:
#         break
#     print(i)

# 3. Print numbers from 1 to 50 and stop when the first number with exactly 3 factors is found.

# for i in range(1,51,1):
#     count=0
#     for j in range(1,i+1,1):
#         if i % j ==0:
#             count+=1
#     if count==3:
#         print(i)
#         break

# 4. Print numbers from 1 to 100 and stop when the first perfect number is found.

# for i in range(1,101,1):
#     sum=0
#     for j in range(1,i,1):
#         if i % j==0:
#             sum=sum+j
#     if sum==i:
#         print(i)
#         break

# 5. Print numbers from 1 to 100 and stop when the first number whose reverse is greater than the original number is found.

# for i in range(1,101,1):
#     n=i
#     rev=0
#     while n>0:
#         digit=n % 10
#         rev=rev*10+digit
#         n= n//10
#     if rev > i:
#         print(i)
#         break

# 6. Print multiples of 3 from 1 to 100 and stop when the printed value becomes greater than 30.

# for i in range(1,101,1):
#     if i%3==0:
#         if i > 30:
#             break
#         print(i)
    
