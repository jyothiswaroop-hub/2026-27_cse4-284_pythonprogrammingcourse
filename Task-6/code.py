
# Warehouse Inventory Reconciliation

inventory = []

print("===== WAREHOUSE INVENTORY RECONCILIATION =====")

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nEnter details for Product", i + 1)

    product_id = input("Product ID: ")
    product_name = input("Product Name: ")

    opening = int(input("Opening Stock: "))
    incoming = int(input("Incoming Quantity: "))
    dispatched = int(input("Dispatched Quantity: "))
    actual_closing = int(input("Actual Closing Stock: "))
    minimum_stock = int(input("Minimum Stock Level: "))

    # Calculate expected closing stock
    expected = opening + incoming - dispatched

    # Calculate discrepancy
    discrepancy = actual_closing - expected

    # Identify stock status
    if discrepancy == 0:
        status = "Matched"
    elif discrepancy > 0:
        status = "Excess Stock"
    else:
        status = "Stock Shortage"

    # Calculate replenishment requirement
    replenishment = max(0, minimum_stock - actual_closing)

    # Store product information
    inventory.append([
        product_id,
        product_name,
        opening,
        incoming,
        dispatched,
        expected,
        actual_closing,
        discrepancy,
        status,
        replenishment
    ])

# Generate final report
print("\n========== INVENTORY REPORT ==========")

print("{:<8} {:<12} {:<10} {:<10} {:<10} {:<10} {:<12} {:<10}".format(
    "ID", "Product", "Opening", "Incoming", "Dispatch",
    "Expected", "Actual", "Difference"
))

for item in inventory:
    print("{:<8} {:<12} {:<10} {:<10} {:<10} {:<10} {:<12} {:<10}".format(
        item[0], item[1], item[2], item[3],
        item[4], item[5], item[6], item[7]
    ))

    print("Status:", item[8])
    print("Replenishment Required:", item[9])
    print("--------------------------------------")

# Summary
total_products = len(inventory)
matched = sum(1 for item in inventory if item[7] == 0)
shortage = sum(1 for item in inventory if item[7] < 0)
excess = sum(1 for item in inventory if item[7] > 0)
total_replenishment = sum(item[9] for item in inventory)

print("\n========== FINAL SUMMARY ==========")
print("Total Products:", total_products)
print("Matched Products:", matched)
print("Products with Shortage:", shortage)
print("Products with Excess:", excess)
print("Total Replenishment Required:", total_replenishment)

print("\nInventory Reconciliation Completed!")

