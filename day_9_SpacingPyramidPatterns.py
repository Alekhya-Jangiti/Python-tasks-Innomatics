# 1. Print a hollow square star pattern of N rows and N columns.

# for i in range(1,10,1):
#     for j in range(1,6,1):
#         if i==1 or i==9 or((i==3 or i==5 or i==7) and (j==1 or j==5)) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 2. Print a hollow right-angled triangle star pattern of N rows.

# for i in range(1,6,1):
#     for j in range(1,i+1,1):
#         if j==1 or j==i or i==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 3. Print a hollow inverted right-angled triangle star pattern of N rows.

# for i in range(5,0,-1):
#     for j in range(1,i+1,1):
#         if j==1 or j==i or i==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 4. Print an X star pattern of N rows and N columns.

# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if i==j or i+j==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 5. Print a plus (+) star pattern of N rows and N columns.

# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if i==3 or j==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# 6. Print a star pattern in the shape of four arrows meeting at the center.

for i in range(1,8,1):
    for j in range(1,8,1):
        if i==4 or j==4 or (j==1 and i<=4) or (i==1 and j>=4) or (j==7 and i>=4) or (i==7 and j<=4):
            print("*",end=" ") 
        else:
            print(" ", end=" ")
    print()
