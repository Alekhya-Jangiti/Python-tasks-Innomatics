#------------------------------------------------if-else-----------------------------------------------------

# 1.Check whether a given number is a 3-digit number or not.
n=int(input("Enter a number :"))
if(n>=100 and n<=999):
    print("Given number is 3 digit number")
else:
    print("Not a 3 digit number")

# 2.Check whether a given number is divisible by both 3 and 5 or not.
n=int(input("Enter a number :"))
if(n%3==0 and n%5==0):
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")

# 3.Check whether a given triangle is a valid triangle or not.
s1=int(input("Enter side 1 :"))
s2=int(input("Enter side 2 :"))
s3=int(input("Enter side 3 :"))
if(s1+s2 > s3 and s2+s3 > s1 and s1+s3 > s2):
    print("Given triangle is valid")
else:
    print("Not a triangle")

# 4.Check whether a given number is a multiple of 10 or not.
n=int(input("Enter a number :"))
if(n%10==0):
    print("Given number is Multiple of 10")
else:
    print("Given number is Not Multiple of 10")

#--------------------------------------------------if-elif-else-----------------------------------------------------
# 1.Check the type of triangle based on its sides.
s1=int(input("Enter side1 of triangle :"))
s2=int(input("Enter side2 of triangle :"))
s3=int(input("Enter side3 of triangle :"))
if(s1==s2 and s2==s3):
    print("Equalient Triangle")
elif(s1==s2 or s2==s3 or s1==s3):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# 2.Calculate the electricity bill based on units consumed.
units=int(input("Enter number of units consumed :"))
if(units>=0 and units<=100):
    print("₹2/unit")
elif(units>=101 and units<=200):
    print("₹3/unit")
elif(units>=201 and units<=300):
    print("₹5/unit")
else:
    print("₹7/unit")

# 3.Display the age category.
age=int(input("Enter an age :"))
if(age<=13):
    print("Child")
elif(age>=13 and age<=19):
    print("Teenager")
elif(age>=20 and age<=59):
    print("Adult")
else:
    print("Senior Citizen")

# 4.Calculate the discount based on shopping amount.
amt=int(input("Enter amount :"))
if(amt<1000):
    print("No discount")
    print(f"Total Amount to pay {amt}")
elif(amt>=1000 and amt<=4999):
    dis=(10/100)*amt
    print(f"Discount is {dis}")
    print(f"Total Amount to pay {amt-dis}")
elif(amt>=5000 and amt<=9999):
    dis=(20/100)*amt
    print(f"Discount is {dis}")
    print(f"Total Amount to pay {amt-dis}")
else:
    dis=(30/100)*amt
    print(f"Discount is {dis}")
    print(f"Total Amount to pay {amt-dis}")
    
#5.Display the season based on the month number.
month=int(input("Enter month number :"))
if(month==3 or month==4 or month==5):
    print("Spring")
elif(month==6 or month==7 or month==8):
    print("Summer")
elif(month==9 or month==10 or month==11):
    print("Autumn")
else :
    print("Winter")

#6.Check whether a given year is a Leap Year or not.
year=int(input("Enter Year :"))
if(year%400==0):
    print("leap year")
elif(year%4==0 or year%100==0):
    print("leap year")
else:
    print("not a leap year")
    
#--------------------------------------------------Nested if – Tasks--------------------------------------------------------
# 1.Check whether a person is eligible to donate blood.
age=int(input("Enter age :"))
if(age>=18 and age<=60):
    weight=int(input("Enter weight :"))
    if(weight>=50):
        print("Eligible to donate blood")
    else:
        print("Not eligible to donate blood")
else:
    print("Not eligible")

# 2.Display the grade based on average only if the student has passed in all 4 subjects.
py=int(input("Enter python marks :"))
m=int(input("Enter maths marks :"))
e=int(input("Enter english marks :"))
sql=int(input("Enter sql marks :"))
avg=(py+m+e+sql)/4
print(f"Average: {avg}")
if(py>=35 and m>=35 and e>=35 and sql>=35):
    if(avg>=90):
        print("O")
    elif(avg>=80):
        print("A")
    elif(avg>=70):
        print("B")
    elif(avg>=60):
        print("C")
    elif(avg>=50):
        print("D")
    else:
        print("E")
else:
    print("Failed")

# 3.Check whether a student is eligible for a scholarship.
age=int(input("Enter age :"))
if(age>=18):
    print("Eligible for scholarship")
    score=int(input("Enter score :"))
    if(score>=86):
        print("Eligible by age")
    else:
        print("Not eligible by age")
else:
    print("Not eligible for schlorship")

        