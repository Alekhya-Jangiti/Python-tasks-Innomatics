
# 1. Print numbers from 1 to 10 and skip the number 5.

# for i in range(1, 11):
#     if i==5:
#         continue
#     print(i)
    
# 2. Extract 502304, skipping digit 0.

# n = 502304
# while n > 0:
#     digit = n%10
#     n = n//10
#     if digit == 0:
#         continue
#     print(digit,end=" ")

# 3. Extract 5832461, printing only even digits.

# n = 5832461
# while n > 0:
#     digit = n%10
#     n = n//10
#     if digit%2!= 0:
#         continue
#     print(digit,end=" ")

# 4. Print 1–50, skipping numbers with odd digit sum.

# for i in range(1,51):
#     n=i
#     sum=0
#     while n > 0:
#         digit = n%10
#         sum = sum+digit
#         n = n//10
#     if sum % 2 != 0:
#         continue
#     print(i,end=" ")

# 5. Print 1–50, skip multiples of 3, stop at 40.

# for i in range(1,51):
#     if i==40:
#         break
#     if i%3==0:
#         continue
#     print(i,end=" ")

# 6. Print numbers from 1 to 50 and skip numbers whose digit sum is divisible by 3.

for i in range(1, 51):
    n = i
    sum = 0
    while n > 0:
        digit = n%10
        sum = sum+digit
        n = n//10
    if sum % 3 == 0:
        continue
    print(i, end=" ")