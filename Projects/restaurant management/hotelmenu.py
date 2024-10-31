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
    item = input(" Enter the item Name you want to oder (close for exit) : ")

    if item in menu.keys():
        order_total += menu[item]
    elif item == 'close':
        print("Your order is added : ", order_total)
        if input(" Like to give us Tip ('yes or no'): ") == 'yes':
            tip = int(input(" Enter the Tip : "))
            total = tip + order_total
            print("Your total Bill is : ", total)
            break;
        else:
            print("Your total Bill is", order_total)
            break;
    else:
        print("Item not found in menu.")
        print("please enter somehting new")