

applicants = []
eligible = []
rejected = []

MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

n = int(input("Enter number of applicants: "))


for i in range(n):

    print("\nEnter details of Applicant", i + 1)

    app_id = int(input("Applicant ID: "))
    name = input("Applicant Name: ")

    marks = []

    print("Enter marks in 5 subjects:")

    for j in range(5):
        mark = float(input(f"Subject {j + 1}: "))

        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")

        marks.append(mark)

    attendance = float(input("Attendance Percentage: "))
    income = float(input("Annual Family Income: "))

    if not 0 <= attendance <= 100:
        raise ValueError("Attendance must be between 0 and 100.")

    if income < 0:
        raise ValueError("Income cannot be negative.")

    aggregate = sum(marks) / len(marks)

   
    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if any(mark < MIN_SUBJECT_MARKS for mark in marks):
        reasons.append("Subject marks below 40")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income > MAX_INCOME:
        reasons.append("Family income exceeds Rs. 2,50,000")

    applicant = {
        "id": app_id,
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income
    }

    if len(reasons) == 0:
        eligible.append(applicant)
    else:
        applicant["reasons"] = reasons
        rejected.append(applicant)


# Sort Eligible Applicants
# 1. Higher aggregate
# 2. Higher attendance
# 3. Lower family income
# 4. Lower applicant ID

eligible.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["id"]
    )
)


print("\n========== SCHOLARSHIP ALLOCATION REPORT ==========")

print("\nELIGIBLE APPLICANTS")

if eligible:
    print("-" * 75)
    print(f"{'Rank':<8}{'ID':<10}{'Name':<15}"
          f"{'Aggregate':<13}{'Attendance':<13}{'Income'}")
    print("-" * 75)

    for rank, student in enumerate(eligible, start=1):
        print(
            f"{rank:<8}"
            f"{student['id']:<10}"
            f"{student['name']:<15}"
            f"{student['aggregate']:<13.2f}"
            f"{student['attendance']:<13.2f}"
            f"Rs.{student['income']:.2f}"
        )
else:
    print("No eligible applicants found.")


# Display Rejected Applicants
print("\nREJECTED APPLICANTS")

if rejected:
    for student in rejected:
        print(f"\nID: {student['id']}")
        print(f"Name: {student['name']}")
        print("Reason(s):", ", ".join(student["reasons"]))
else:
    print("No rejected applicants.")

print("\n========== END OF REPORT ==========")

