# for i in range(1,8,1):
#     for j in range(1,8,1):
#         if i==4 or j==4 or (j==1 and i<=4) or (i==1 and j>=4) or (j==7 and i>=4) or (i==7 and j<=4):
#             print("*",end=" ") 
#         else:
#             print(" ", end=" ")
#     print()
# *     * * * * 
# *     *       
# *     *       
# * * * * * * * 
#       *     * 
#       *     * 
# * * * *     * 

for i in range(1,8,1):
    for j in range(1,8,1):
        if (i==1 and j==4) or (i==4 and i<=j<=8) or (i==5 and j==1 or j==8) or (i==4 and j==3) or (i==4 and j==4) or (i==4 and j==5) or (i==4 and j==6):
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print()
    