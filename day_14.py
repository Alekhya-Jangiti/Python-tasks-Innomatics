
# 1. Create a function to calculate the simple interest.

# def simple_interest(p,t,r):
#     si=(p * t* r)/100
#     print(f"Simple Interest = ",si)
# simple_interest(5000,2,5)

# 2. Create a function to calculate the final price after applying a discount.

# def final_price(price,discount):
#     amount= (price * discount) /100
#     return price - amount
# res=final_price(2000,15)
# print(res)

# 3. Create a function to convert Celsius temperature to Fahrenheit.

# def temperature(c):
#     return (c * 9/5) + 32
# res=temperature(30)
# print(f"Celsius to Fahrenheit : {res}")

# 4. Calculate delivery charge based on distance

# def delivery_charge(distance):
#     if distance <= 5 :
#         charge = 40
#     elif distance <= 10:
#         charge = 70
#     else : 
#         charge = 100
#     return charge
# res=delivery_charge(8)
# print(f"Charge = {res}")

# 5. Calculate profit or loss and how much hey gained or lose

# def profit_loss(cp,sp):
#     if sp > cp:
#         print("Profit =",end= " ")
#         profit = sp - cp
#         return profit
#     elif sp < cp:
#         print("Loss = ", end=" ")
#         loss= cp - sp
#         return loss
#     else:
#         return "No Profit No Loss"
# res=profit_loss(500,300)
# print(res)

# 6. Find the middle number among three numbers

# def middle_num(a, b, c):
#     if (a > b and a < c) or (a < b and a >c):
#         return a
#     elif (b > a and b < c) or (b < a and b > c):
#         return b
#     else:
#         return c
# res=middle_num(5,12,22)
# print(f"Middle number among three numbers is {res}")

# 1. Return quotient and remainder

# def divide(n1, n2): 
#     quotient = n1 // n2
#     remainder = n1 % n2
#     return quotient, remainder
# q, r=divide(17,5)
# print(f" Quotient = {q}\n Remainder = {r}")