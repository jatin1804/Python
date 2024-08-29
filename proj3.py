# hotel menu
menu = {
    'Pizza': 40,
    'Pasta': 80,
    'Burger': 70,
    'Salad': 60,
    'Cold Coffee': 90,
}

# Greeting the customer
print("Welcome to Python restaurant")
print("Pizza: Rs40\nPasta: Rs80\nBurger: Rs70\nSalad: Rs60\nCold Coffee: Rs90")

order_Total = 0

# Taking the first item order
item_1 = input("Enter your order: ")
if item_1 in menu:
    order_Total += menu[item_1]
    print(f"Your item {item_1} has been added.")
else:
    print("Please order something else we can serve you.")

# Asking if the customer wants to order something else
another_item = input("Do you want to order something else? (Yes/No): ").strip().capitalize()
if another_item == "Yes":
    item_2 = input("What else do you want to add to the order? ")
    if item_2 in menu:
        order_Total += menu[item_2]
        print(f"Another dish {item_2} has been added to your order.")
    else:
        print(f"Item {item_2} not available.")
else:
    print("No additional items added.")

# Printing the total amount of the order
print(f"Total amount of your order is Rs{order_Total}")
