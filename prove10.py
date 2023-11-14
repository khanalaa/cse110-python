# NAME: Aayush Khanal

print("Welcome to the Shopping Cart Program!\n")

print('''Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
      ''')

item = []
prices = []
quantities = []
total = []
choice = int(input("Please enter an action: "))

while choice != 5:
    if choice == 1:
        item_name = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item_name}'? "))
        quantity = int(input(f"Enter the number of {item_name}. "))
        print(f"{quantity} '{item_name}' has been added to the cart.\n")
        item.append(item_name)
        prices.append(price)
        quantities.append(quantity)
        total.append(price * quantity)

    elif choice == 2:
        print("The contents of the shopping cart are:")
        for index, (item_name,price,quantity) in enumerate(zip(item, prices,quantities)):
            print(f"{index + 1}. {quantity} {item_name} - ${price} each\n")

    elif choice == 3:
        remove = int(input("Which item would you like to remove? ")) - 1
        item.pop(remove)
        prices.pop(remove)
        quantities.pop(remove)
        total.pop(remove)
        print("Item removed.\n")

    elif choice == 4:
        final_total = sum(total)
        print(f"The total price of items in the cart is: ${final_total}\n")

    print('''Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
      ''')
    choice = int(input("Please enter an action: "))


print("Thank You. Goodbye.")