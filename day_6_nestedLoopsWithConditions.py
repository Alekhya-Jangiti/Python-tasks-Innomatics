# 1. Print all two-digit numbers whose digits add up to 10.

# n=10
# for i in range(1,n+1,1):
#     for j in range(0,n+1,1):
#         if i+j==n: 
#             print(f"{i}{j}",end="  ")

# 2. Print all two-digit numbers whose digits multiply to 12.

# n=12
# for i in range(1,n+1,1):
#     for j in range(0,n+1,1):
#         if i*j==n: 
#             print(f"{i}{j}",end="  ")

# 3. Print all three-digit numbers whose digits are in increasing order.

# n=10
# for i in range(1,n,1):
#     for j in range(0,n,1):
#         for k in range(0,n,1):
#             if i<j and j<k:
#                 print(f"{i}{j}{k}",end="  ")

# 4. Print all three-digit numbers whose digits are in decreasing order.

# n=10
# for i in range(1,n,1):
#     for j in range(0,n,1):
#         for k in range(0,n,1):
#             if i>j and j>k:
#                 print(f"{i}{j}{k}",end="  ")
                
# 5. Print all two-digit numbers having no repeated digits.

# n=10
# for i in range(1,n,1):
#     for j in range(1,n,1):
#             if i!=j :
#                 print(f"{i}{j}",end="  ")

# 6. Print all three-digit numbers having at least one repeated digit.

n=10
for i in range(1,n,1):
    for j in range(0,n,1):
        for k in range(0,n,1):
            if i==j or j==k or i==k:
                print(f"{i}{j}{k}",end="  ")
