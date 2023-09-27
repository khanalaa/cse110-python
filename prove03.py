child_meal = float(input("What is the price of a child's meal? "))
adutl_meal = float(input("What is the price of an adult's meal? "))
childrenNum = int (input("How many children are there? "))
adultNum = int(input("How many adults are there? "))
tax = int(input("What is the sales tax rate? "))

subtotal = (child_meal * childrenNum) + (adutl_meal * adultNum)
taxAmount = (tax/100) * subtotal
total = subtotal + taxAmount

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${taxAmount:.2f}")
print(f"Total: ${total:.2f}")

payment = float (input("\nWhat is the payment amount? "))

change = payment - total

print(f"Change: ${change:.2f}")


