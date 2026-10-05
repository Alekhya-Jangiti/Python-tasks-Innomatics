
# 1. 
#   1 1 1 1 1 
#   2 2 2 2 2 
#   3 3 3 3 3 
#   4 4 4 4 4 
#   5 5 5 5 5 

# for i in range(1,6,1):
#     for j in range(1,6,1):
#         print(i,end=" ")
#     print()

# 2. 
#   1 1 1 1 1 
#   0 0 0 0 0 
#   1 1 1 1 1 
#   0 0 0 0 0 
#   1 1 1 1 1 

# for i in range(1,6,1):
#     for j in range(1,6,1):
#         print(i%2,end=" ")
#     print()

# 3. 
#    1 
#    1 2 
#    1 2 3 
#    1 2 3 4 
#    1 2 3 4 5 

# for i in range(1,6,1):
#     for j in range(1,i+1,1):
#         print(j,end=" ")
#     print()

# 4. 
#    5 4 3 2 1 
#    4 3 2 1 
#    3 2 1 
#    2 1 
#    1 

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# 5.
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

# for i in range(1,6,1):
#     for s in range(5,i,-1):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 6.
#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5

for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,1-1,-1):
        print(j,end=" ")
    for k in range(2,i+1,1):
        print(k,end=" ")
    print()
