#Find the average of three numbers
# n1=int(input("Enter num1:"))
# n2=int(input("Enter num2:"))
# n3=int(input("Enter num3:"))
# avg=(n1+n2+n3)/3
# print("Average :",avg)

#Find the profit percentage by using selling price & cost price
# cp=int(input("Enter Cost Price :"))
# sp=int(input("Enter Selling Price :"))
# profit=sp-cp
# print("Profit =",profit)
# profit_per=(profit//cp)*100
# print("profit percentage =",profit_per,"%")

#Find the missing angle in the triangle
# n1=int(input("Enter first angle :"))
# n2=int(input("Enter second angle :"))
# n3=180-(n1+n2)
# print("Third angle is :",n3)

#find the last digit of given number
# n=int(input("Enter number :"))
# res=n%10
# print(res)

#Remove last digit of given number
# n=int(input("Enter number :"))
# res=n//10
# print(res)

#find the first digit of four digit number
# n=int(input("Enter 4 digit number :"))
# res=n//1000
# print(res)

#find the sum of first n natural numbers
# n=int(input("Enter number :"))
# sum=0
# sum=(n*(n+1))//2
# print("Sum of first 10 natural numbers is :",sum)


#find the avg of first 10 natural numbers
# n=int(input("Enter number :"))
# sum=0
# sum=(n*(n+1))//2
# avg=sum/n
# print("Average of first 10 natural numbers is :",avg)

#find gross salary
# bs=int(input("Enter basic salary :"))
# b=int(input("Enter bonus  :"))
# i=int(input("Enter Incentive salary :"))
# bonus=(b/100)*bs
# incentive=(i/100)*bs
# print(bonus)
# print(incentive)
# gross_salary=bs+bonus+incentive
# print("Gross Salary :",gross_salary)

#find inhand salary
# bs=int(input("Enter basic salary :"))
# b=int(input("Enter bonus  :"))
# i=int(input("Enter Incentive salary :"))
# pf=int(input("Enter PF :"))
# hi=int(input("Enter health insurance :"))
# bonus=(b/100)*bs
# incentive=(i/100)*bs
# h=(hi/100)*bs
# p=(pf/100)*bs
# print(bonus)
# print(incentive)
# gross_salary=bs+bonus+incentive
# inhand=gross_salary-(h+p)
# print("Gross Salary :",gross_salary)

#swap 2 numbers by using 3 variables
# a=int(input("Enter num1 :"))
# b=int(input("Enter num2 :"))
# print("Before swapping")
# print("a=",a)
# print("b=",b)
# temp=a
# a=b
# b=temp
# print("After swapping")
# print("a=",a)
# print("b=",b)

#swap 2 numbers by using 2 variables
# a=int(input("Enter num1 :"))
# b=int(input("Enter num2 :"))
# print("Before swapping")
# a=a+b
# b=a-b
# a=a-b
#or
# a=a*b
# b=a//b
# a=a//b

# print("After swapping")
# print("a=",a)
# print("b=",b)


n=int(input("Enter num :"))
if n%10==0 or n%10==2 or n%10==4 or n%10==6 or n%10==8:
    print("Even num")
else:
    print("odd num")