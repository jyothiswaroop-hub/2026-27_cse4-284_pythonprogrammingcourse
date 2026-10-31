
products = {
    101: {"name": "Laptop", "price": 50000, "stock": 10},
    102: {"name": "Mobile", "price": 20000, "stock": 15},
    103: {"name": "Headphones", "price": 2000, "stock": 20}
}

initial_stock = {
    pid: details["stock"]
    for pid, details in products.items()
}

dispatched = {pid: 0 for pid in products}
returned = {pid: 0 for pid in products}

total_revenue = 0
order_count = int(input("Enter number of orders: "))

for i in range(order_count):

    print("\n--- ORDER", i + 1, "---")

    order_id = input("Enter Order ID: ")
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity: "))

    if product_id not in products:
        print("Invalid Product ID")
        continue

    product = products[product_id]

    if quantity <= 0:
        print("Invalid quantity")
        continue

    if quantity > product["stock"]:
        print("Insufficient stock")
        continue

    # Calculate order amount
    amount = product["price"] * quantity

    # Apply discount
    if amount >= 50000:
        discount = amount * 0.10
    elif amount >= 20000:
        discount = amount * 0.05
    else:
        discount = 0

    final_amount = amount - discount

    # Dispatch order
    product["stock"] -= quantity
    dispatched[product_id] += quantity

    total_revenue += final_amount

    print("\nOrder ID:", order_id)
    print("Product:", product["name"])
    print("Original Amount: Rs.", amount)
    print("Discount: Rs.", discount)
    print("Final Amount: Rs.", final_amount)
    print("Dispatch Status: Successful")

    # Process return
    return_qty = int(
        input("Enter returned quantity (0 if none): ")
    )

    if return_qty < 0 or return_qty > quantity:
        print("Invalid return quantity")
    elif return_qty > 0:

        refund = (final_amount / quantity) * return_qty

        product["stock"] += return_qty
        returned[product_id] += return_qty
        total_revenue -= refund

        print("Return Status: Successful")
        print("Refund Amount: Rs.", round(refund, 2))

    else:
        print("No returns")

print("\n========== INVENTORY RECONCILIATION ==========")

for pid, product in products.items():

    expected_stock = (
        initial_stock[pid]
        - dispatched[pid]
        + returned[pid]
    )

    actual_stock = product["stock"]

    discrepancy = expected_stock - actual_stock

    print("\nProduct:", product["name"])
    print("Initial Stock:", initial_stock[pid])
    print("Dispatched:", dispatched[pid])
    print("Returned:", returned[pid])
    print("Expected Stock:", expected_stock)
    print("Actual Stock:", actual_stock)

    if discrepancy == 0:
        print("Discrepancy: None")
    else:
        print("Discrepancy:", discrepancy)

# Final summary
print("\n========== FINAL SUMMARY ==========")

print("Total Orders:", order_count)
print("Total Revenue: Rs.", round(total_revenue, 2))

print("\nFinal Inventory:")

for pid, product in products.items():
    print(
        product["name"],
        "- Available Stock:",
        product["stock"]
    )

print("\nOrder Processing Completed!")

