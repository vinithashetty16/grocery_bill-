# Grocery Billing system

# store item as a list of dictionaries
def generate_bill():
 item = []

 print("============Welcome to the Grocery Billing system===========")

# Take input for grocery items 
while True:
    name = input("Enter item name or 'done' to finish): ")
    if name.lower() == 'done':
     break
    try:
     quantity = int(input(f"Enter quantity for {name}: "))
     price = float(input(f"Enter price per unit for {name}: "))
    except ValueError:
     print("Please enter valid quantity (int) and price (float).\n")
     continue

    total = quantity * price
    items.append({
      "name": name,
      "quantity": quantity,
      "price": price,
      "total": total
    })
    print(f"{name} added to bill.\n")
 #print the final bill
    print("\n=============GROCERY BILL==============")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Price", "Total"))

    print("-----------------------------------------------------------")

    grand_total = 0
    for item in items:
      print("{:<15} {:<10} {:<10.2f} {:<10.2f}".format(
       item ["name"], item["quantity"], item["price"], item["total"]))
    grand_total += item["total"]

    print("-------------------------------------------------------------")
    print(f"Grand Total: ₹{grand_total :.2f}")

    print("===============================================================")

#Run the function
generate_bill()
