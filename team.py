print("Welcome to the Shopping Cart Program!\n")

print('''Please select one of the following:\n 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
      ''')

item = []
prices = []
choice = int(input("Please enter an action: "))

while choice != 5:
    if choice == 1:
        item_name = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item_name}'? "))
        print(f"'{item_name}' has been added to the cart.")
        item.append(item_name)
        prices.append(price)

    elif choice == 2:
        print("The contents of the shopping cart are:")
        for index, (item_name,price) in enumerate(zip(item, prices)):
            print(f"{index + 1}. {item_name} - ${price}\n")

    elif choice == 3:
        remove = int(input("Which item would you like to remove? ")) - 1
        item.pop(remove)
        prices.pop(remove)
        print("Item removed.")

    elif choice == 4:
        total = sum(prices)
        print(f"The total price of items in the cart is: ${total}")

    print('''Please select one of the following:\n 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
      ''')
    choice = int(input("Please enter an action: "))


print("Thank You. Goodbye.")