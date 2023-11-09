print("Welcome to the Shopping Cart Program!\n")

print('''Please select one of the following:\n 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit''')

item = []
choice = int(input("Please enter an action: "))

while choice != 5:
    if choice == 1:
        item_name = input("What item would you like to add? ")
        print(f"'{item_name}' has been added to the cart.")
        item.append(item_name)

        print('''\nPlease select one of the following:\n 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit''')
        choice = int(input("Please enter an action: "))

    if choice == 2:
        sorted_item = sorted(item)
        print("The contents of the shopping cart are:")
        for item in sorted_item:
            print(f"{item}")

        print('''\nPlease select one of the following:\n 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit''')
        choice = int(input("Please enter an action: "))
        

print("Thank You. Goodbye.")

