# 1. Print all pairs of numbers whose sum is equal to a given number

n=20
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if i+j==n and i<=j:
#             print(f"{i} {j}")

# 2. Print all pairs where the first number is smaller than the second number.

# n1=10
# n2=15
# for i in range(n1,n2+1,1):
#     for j in range(n1,n2+1,1):
#         if i<j:
#             print(f"{i} {j}")

# 3. Print all pairs whose product is even.

# n=5
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if (i%2==0 or j%2==0) and i<=j:
#                 print(f"{i} {j}")

# 4. Print all pairs where one number is exactly divisible by the other.

# n=5
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if (i%j==0 or j%i==0):
#             print(f"{i} {j}")

# 5. Print all pairs of numbers from 1 to 15 where both numbers 
# are different and their last digits are the same.

# n=15
# for i in range(1,n+1,1):
#     for j in range(1,n+1,1):
#         if (i!=j and i%10 == j%10):
#             print(f"{i} {j}")

# 6. Print all pairs of numbers from 1 to 5 where the 
# first number is odd and the second number is even.

n=5
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if i%2!=0 and j%2==0:
            print(f"{i} {j}") 
