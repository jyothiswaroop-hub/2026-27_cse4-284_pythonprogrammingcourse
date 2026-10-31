

def calculate_bill(units):
    bill = 0

   
    if units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed monthly charge
    fixed_charge = 50

    total = bill + fixed_charge

    # Apply 5% rebate for consumption below 100 units
    rebate = 0

    if units < 100:
        rebate = total * 0.05

    final_bill = total - rebate

    return bill, fixed_charge, rebate, final_bill


apartments = []

n = int(input("Enter number of apartments: "))

for i in range(n):
    print("\nEnter details of Apartment", i + 1)

    apt_id = input("Apartment ID: ")
    name = input("Resident Name: ")
    units = int(input("Units Consumed: "))
    recorded_bill = float(input("Recorded Bill Amount: "))

    energy, fixed, rebate, final = calculate_bill(units)

    difference = abs(final - recorded_bill)

    if difference > 0.01:
        status = "Discrepancy Found"
    else:
        status = "Bill Verified"

    apartments.append({
        "id": apt_id,
        "name": name,
        "units": units,
        "energy": energy,
        "fixed": fixed,
        "rebate": rebate,
        "final": final,
        "recorded": recorded_bill,
        "difference": difference,
        "status": status
    })


# Display apartment-wise billing report
print("\n========== ELECTRICITY BILLING REPORT ==========")

for apt in apartments:
    print("\nApartment ID:", apt["id"])
    print("Resident Name:", apt["name"])
    print("Units Consumed:", apt["units"])
    print("Energy Charges: Rs.", round(apt["energy"], 2))
    print("Fixed Charges: Rs.", round(apt["fixed"], 2))
    print("Rebate: Rs.", round(apt["rebate"], 2))
    print("Calculated Bill: Rs.", round(apt["final"], 2))
    print("Recorded Bill: Rs.", round(apt["recorded"], 2))
    print("Difference: Rs.", round(apt["difference"], 2))
    print("Status:", apt["status"])


# Rank apartments by consumption
ranked = sorted(
    apartments,
    key=lambda x: x["units"],
    reverse=True
)

print("\n========== CONSUMPTION RANKING ==========")

for rank, apt in enumerate(ranked, start=1):
    print(
        rank, ".", apt["id"],
        "-", apt["name"],
        "-", apt["units"], "units"
    )

print("\n========== BILLING SUMMARY ==========")

discrepancies = sum(
    1 for apt in apartments
    if apt["status"] == "Discrepancy Found"
)

print("Total Apartments:", n)
print("Verified Bills:", n - discrepancies)
print("Discrepant Bills:", discrepancies)

print("\nElectricity Billing Process Completed!")

