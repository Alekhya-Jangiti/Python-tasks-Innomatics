
# 1. Create a function to print numbers from 1 to 10.

# def numbers():
#     for i in range(1, 11):
#         print(i, end=" ")
# numbers()

# 2. Create a function to find the sum of numbers from 1 to N.

# def total(n):
#     sum = 0
#     for i in range(1, n+1, 1):
#         sum = sum + i
#     print(sum)
# total(10)

# 3. Create a function to check whether a number is prime.

# def prime(n):
#     count=0
#     for i in range(1,n+1, 1):
#         if n % i ==0:
#             count+=1
#     if count ==2 :
#         print("prime")
#     else:
#         print("nor prime")
# prime(7)

# 4. Create a function that accepts a number and returns the number of digits.

# def count_digits(n):
#     count = 0
#     while n > 0:
#         count = count + 1
#         n = n // 10
#     return count
# res = count_digits(583246)
# print(res)

# 5. Create a function that accepts a number and returns its reverse.

# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10
#     return rev
# res = reverse_number(5832)
# print(res)

# 6. Return the difference between largest and smallest digit.

def difference(n):
    largest = 0
    smallest = 9
    while n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        n = n // 10
    return largest - smallest
res = difference(583246)
print(res)
