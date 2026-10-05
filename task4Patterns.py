for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i,end=" ")
    print()
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end=" ")
    print()
# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 

for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print(i,end=" ")
    print()
#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 

for i in range(5,0,-1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(i,end=" ")
    print()
# 5 5 5 5 5 
#   4 4 4 4 
#     3 3 3 
#       2 2 
#         1 

for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(i,end=" ")
    for k in range(2,i+1,1):
        print(i,end=" ")
    print()
#         1 
#       2 2 2 
#     3 3 3 3 3 
#   4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 

for i in range(5,0,-1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(i,end=" ")
    for k in range(2,i+1,1):
        print(i,end=" ")
    print()
# 5 5 5 5 5 5 5 5 5 
#   4 4 4 4 4 4 4 
#     3 3 3 3 3 
#       2 2 2 
#         1 

for i in range(5,0,-1):
    for s in range(2,i+1,1):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print(i,end=" ")
    for k in range(4,i-1,-1):
        print(i,end=" ")
    print()
#         5 
#       4 4 4 
#     3 3 3 3 3 
#   2 2 2 2 2 2 2 
# 1 1 1 1 1 1 1 1 1 

for i in range(1,6,1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print(i,end=" ")
    for k in range(4,i-1,-1):
        print(i,end=" ")
    print()
# 1 1 1 1 1 1 1 1 1 
#   2 2 2 2 2 2 2 
#     3 3 3 3 3 
#       4 4 4 
#         5 

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
# 5 
# 5 4 
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1 

for i in range(1,6,1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

for i in range(5,0,-1):
    for j in range(i,6,1):
        print(j,end=" ")
    print()
# 5 
# 4 5 
# 3 4 5 
# 2 3 4 5 
# 1 2 3 4 5 

for i in range(1,6,1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 

for i in range(5,0,-1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

for i in range(1,6,1):
    for j in range(i,6,1):
        print(j,end=" ")
    print()
# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5 

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 

for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 

for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1 

for i in range(5,0,-1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
#         5 
#       5 4 
#     5 4 3 
#   5 4 3 2 
# 5 4 3 2 1 

for i in range(5,0,-1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(i,6,1):
        print(j,end=" ")
    print()
#         5 
#       4 5 
#     3 4 5 
#   2 3 4 5 
# 1 2 3 4 5 

for i in range(1,6,1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
# 5 4 3 2 1 
#   5 4 3 2 
#     5 4 3 
#       5 4 
#         5 

for i in range(5,0,-1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
# 5 4 3 2 1 
#   4 3 2 1 
#     3 2 1 
#       2 1 
#         1 

for i in range(5,0,-1):
    for s in range(5,i-1,-1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
#   1 2 3 4 5 
#     1 2 3 4 
#       1 2 3 
#         1 2 
#           1 

for i in range(1,6,1):
    for s in range(1,i+1,1):
        print(" ",end=" ")
    for j in range(i,6,1):
        print(j,end=" ")
    print()
#   1 2 3 4 5 
#     2 3 4 5 
#       3 4 5 
#         4 5 
#           5 

for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for k in range(2,i+1,1):
        print(k,end=" ")
    print()
#         1 
#       2 1 2 
#     3 2 1 2 3 
#   4 3 2 1 2 3 4 
# 5 4 3 2 1 2 3 4 5 

for i in range(5,0,-1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(i,6,1):
        print(j,end=" ")
    for k in range(4,i-1,-1):
        print(k,end=" ")
    print()
#         5 
#       4 5 4 
#     3 4 5 4 3 
#   2 3 4 5 4 3 2 
# 1 2 3 4 5 4 3 2 1 

for i in range(1,6,1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 

for i in range(5,0,-1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print(j,end=" ")
    for k in range(i+1,6,1):
        print(k,end=" ")
    print()
#         5 
#       5 4 5 
#     5 4 3 4 5 
#   5 4 3 2 3 4 5 
# 5 4 3 2 1 2 3 4 5

for i in range(1,6,1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print(j,end=" ")
    for k in range(i+1,6,1):
        print(k,end=" ")
    print()
# 5 4 3 2 1 2 3 4 5 
#   5 4 3 2 3 4 5 
#     5 4 3 4 5 
#       5 4 5 
#         5 

for i in range(5,0,-1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()
# 1 2 3 4 5 4 3 2 1 
#   1 2 3 4 3 2 1 
#     1 2 3 2 1 
#       1 2 1 
#         1 

for i in range(5,0,-1):
    for s in range(5,i,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for k in range(2,i+1,1):
        print(k,end=" ")
    print()
# 5 4 3 2 1 2 3 4 5 
#   4 3 2 1 2 3 4 
#     3 2 1 2 3 
#       2 1 2 
#         1 

for i in range(1,6,1):
    for s in range(1,i,1):
        print(" ",end=" ")
    for j in range(i,6,1):
        print(j,end=" ")
    for k in range(4,i-1,-1):
        print(k,end=" ")
    print()
# 1 2 3 4 5 4 3 2 1 
#   2 3 4 5 4 3 2 
#     3 4 5 4 3 
#       4 5 4 
#         5 

for i in range(1,8,1):
    for j in range(1,8,1):
        if i==4 or j==4 or (j==1 and i<=4) or (i==1 and j>=4) or (j==7 and i>=4) or (i==7 and j<=4):
            print("*",end=" ") 
        else:
            print(" ", end=" ")
    print()
# *     * * * * 
# *     *       
# *     *       
# * * * * * * * 
#       *     * 
#       *     * 
# * * * *     * 