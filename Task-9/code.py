
# Hospital Resource Allocation and Capacity Monitoring

wards = []

n = int(input("Enter number of wards: "))

for i in range(n):
    print("\nEnter details for Ward", i + 1)

    name = input("Ward Name: ")
    total_beds = int(input("Total Beds: "))
    occupied_beds = int(input("Occupied Beds: "))
    available_staff = int(input("Available Staff: "))
    required_staff = int(input("Required Staff: "))
    available_equipment = int(input("Available Equipment: "))
    required_equipment = int(input("Required Equipment: "))

    # Calculate available beds
    available_beds = total_beds - occupied_beds

    # Identify shortages
    shortages = []

    if available_beds <= 0:
        shortages.append("Beds")

    if available_staff < required_staff:
        shortages.append("Staff")

    if available_equipment < required_equipment:
        shortages.append("Equipment")

    # Assign priority
    if len(shortages) >= 2:
        priority = "High"
        priority_value = 1
    elif len(shortages) == 1:
        priority = "Medium"
        priority_value = 2
    else:
        priority = "Low"
        priority_value = 3

    # Store ward details in nested list
    ward = [
        name,
        [total_beds, occupied_beds, available_beds],
        [available_staff, required_staff],
        [available_equipment, required_equipment],
        shortages,
        priority,
        priority_value
    ]

    wards.append(ward)

# Sort wards based on priority
wards.sort(key=lambda x: x[6])

# Display report
print("\n========== HOSPITAL RESOURCE REPORT ==========")

for ward in wards:
    print("\nWard:", ward[0])
    print("Total Beds:", ward[1][0])
    print("Occupied Beds:", ward[1][1])
    print("Available Beds:", ward[1][2])

    print("Available Staff:", ward[2][0])
    print("Required Staff:", ward[2][1])

    print("Available Equipment:", ward[3][0])
    print("Required Equipment:", ward[3][1])

    if ward[4]:
        print("Resource Shortages:", ", ".join(ward[4]))
    else:
        print("Resource Shortages: None")

    print("Priority:", ward[5])

# Summary
high = sum(1 for w in wards if w[5] == "High")
medium = sum(1 for w in wards if w[5] == "Medium")
low = sum(1 for w in wards if w[5] == "Low")

total_beds = sum(w[1][0] for w in wards)
occupied = sum(w[1][1] for w in wards)
available = sum(w[1][2] for w in wards)

print("\n========== FINAL SUMMARY ==========")
print("Total Wards:", n)
print("Total Beds:", total_beds)
print("Occupied Beds:", occupied)
print("Available Beds:", available)
print("High Priority Wards:", high)
print("Medium Priority Wards:", medium)
print("Low Priority Wards:", low)

print("\nWards are arranged according to resource priority.")

