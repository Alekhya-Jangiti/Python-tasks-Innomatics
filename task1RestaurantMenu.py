print("---------------MENU---------------")
print(" 1.Biryani\n 2.Chicken65\n 3.Veg Pulao \n 4.Butter Chicken\n 5.Paneer Tikka")
choice=int(input("Enter your choice :"))
match choice:
    case 1:
        print(" Item : Biryani\n Price : ₹250\n Description : Fragment basmati rice cooked with spices and chicken. ")
    case 2:
        print(" Item : Chicekn65\n Price : ₹180\n Description : Crispy and spicy deep-fried chicken pieces. ")
    case 3:
        print(" Item : Veg Pulao\n Price : ₹200\n Description :  Fragrant basmati rice cooked with fresh garden vegetables and aromatic whole spices. ")
    case 4:
        print(" Item : Butter Chicken\n Price : ₹280\n Description : Tender tandoori grilled chicken pieces simmered in a velvety, rich tomato and cream-butter gravy. ")
    case 5:
        print(" Item : Panner Tikka\n Price : ₹250\n Description : Spiced cottage cheese cubes grilled with bell peppers and onions to smoky perfection. ")
    case _:
        print("Sorry not available")
    