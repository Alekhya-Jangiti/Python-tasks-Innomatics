# 1.Find the sum of digits in a given number.
# Example: 738 → 7 + 3 + 8 = 18
n=int(input("Enter number :"))
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10  
print(sum)

# 2.Find the average of digits in a given number.
#      Example: 624 → (6 + 2 + 4) / 3 = 4
n=int(input("Enter number :"))
sum=0
count=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
    count+=1
avg=sum/count
print(avg)

# 3.Find the sum of the first digit and the last digit of a given number.
     #Example: 936 → 9 + 6 = 15
n=int(input("Enter number :"))
if n<10:
    print(n)
else:
    last=n%10
    while n>=10:
        n=n//10
    first=n
    print(first+last)

# 4.Find the average of digits that are divisible by 5 in a given number.
#      Example: 12575 → Divisible by 5 digits: 5, 5, 5 → Average = (5 + 5 + 5) / 3 = 5
n=int(input("Enter number :"))
sum=0
count=0
while n>0:
    digit=n%10
    if digit == 5:
        sum=sum+digit
        count+=1
    n=n//10
if count > 0:
    avg = sum / count
    print(avg)
else:
    print("No digit divisible by 5")

# 5.Find the difference between the largest digit and the smallest digit in a given number.
#      Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7
n=int(input("Enter number :"))
large=0
small=9
while n>0:
    digit=n%10
    if digit>large:
        large=digit
    if digit<small:
        small=digit
    n=n//10
print(large)
print(small)
print(large-small) 

    
    