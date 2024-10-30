menu ={
    'Pizza': 60,
    'Burger': 50,
    'Salad': 35,
    'Fries': 55,
    'Drinks': 30,
    'Desert': 50
}


print("Welcome to Next-in retstaurant".center(50,'-'))
print("\nPzza: Rs: 60\nBurger: Rs: 50\nFries: Rs: 55\nDrinks: Rs: 55\nDesert: Rs: 50\nDrinks: Rs: 30\n")

order_total = 1;
while True:
    item1 = input(" Enter the item Name you want to oder : ")

    if item1 in menu.keys():
        order_total += menu[item1]
    elif item1 == 'quit':
        print("Your order is added : ", order_total)
        break;
    else:
        print("Item not found in menu.")
        print("please enter somehting new")