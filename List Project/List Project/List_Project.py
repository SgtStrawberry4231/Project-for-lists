print("Hello welcome to A2 is a trash name")
print("Here are the items on the menu: Pizza, Pie, Burger, Chips, Onion rings and any drink")
print("What would you like to eat")
# The menu and the prices of the items
menu = {
    "Pizza": 7.30,
    "Pie": 3.45,
    "Burger": 4.50,
    "Chips": 2.00,
    "Onion Rings": 2.30,
    "Drink": 1.50
}
 
# Empties the list and stores the recent orders
order = []
 
# stores the cost
total_cost = 0.0
 
# Main loop
while True:
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: £{price:.2f}")
 
    choice = input("What would you like to order (or type 'done' to complete the order): ").strip()
 
    if choice.lower() == 'done':
        break
    # adds the price of the items to the total cost
    if choice in menu:
        order.append(choice)
        total_cost += menu[choice]
        print(f"{choice} your order has been added")
# Shows the price of the entire order that has been ordered
if order:
    print("Your order:")
    for item in order:
        print(item)
        print(f"Total cost: £{total_cost:.2f}")
else:
    print("Sorry we do not have this in stock.")
