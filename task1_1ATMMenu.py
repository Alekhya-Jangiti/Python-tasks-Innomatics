print("------------ATM MENU------------")
print(" 1.Check Balance\n 2.Deposit\n 3.Withdraw \n 4.Exit")
choice=int(input("Enter your choice :"))
bal=10000

match choice:
    case 1:
        print(f"Current Balance :{bal}")
    case 2:
        dep=float(input("Enter deposit amount :"))
        print("Amount deposited successfully.")
        print("Updated Balance  :",bal+dep)
    case 3:
        withdraw=float(input("Enter withdrawl amount :"))
        print("Amount withdrawl successfully.")
        print("Remaining Balance  :",bal-withdraw)
    case 4:
        print("Thank you for using ATM")