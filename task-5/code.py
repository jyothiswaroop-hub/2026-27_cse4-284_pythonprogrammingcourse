
# Student Academic Risk Classification System

names = []
marks = []
attendance = []
lab_scores = []

# Risk category counters
high_risk = 0
moderate_risk = 0
low_risk = 0
no_risk = 0

# Get number of students
n = int(input("Enter number of students: "))

# Input student details
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    attend = float(input("Enter attendance percentage: "))
    lab = float(input("Enter laboratory score: "))

    names.append(name)
    marks.append(mark)
    attendance.append(attend)
    lab_scores.append(lab)

# Academic risk classification
print("\n========== STUDENT RISK REPORT ==========")

for i in range(n):

    risk_factors = []

    # Check marks
    if marks[i] < 40:
        risk_factors.append("Low Marks")

    # Check attendance
    if attendance[i] < 75:
        risk_factors.append("Low Attendance")

    # Check laboratory score
    if lab_scores[i] < 40:
        risk_factors.append("Low Lab Score")

    # Classify risk
    count = len(risk_factors)

    if count == 3:
        category = "High Risk"
        high_risk += 1

    elif count == 2:
        category = "Moderate Risk"
        moderate_risk += 1

    elif count == 1:
        category = "Low Risk"
        low_risk += 1

    else:
        category = "No Risk"
        no_risk += 1

    # Display student report
    print("\nStudent Name:", names[i])
    print("Marks:", marks[i])
    print("Attendance:", attendance[i], "%")
    print("Lab Score:", lab_scores[i])
    print("Risk Factors:",
          ", ".join(risk_factors) if risk_factors else "None")
    print("Risk Category:", category)

# Final summary
print("\n========== FINAL SUMMARY ==========")
print("Total Students:", n)
print("High Risk Students:", high_risk)
print("Moderate Risk Students:", moderate_risk)
print("Low Risk Students:", low_risk)
print("No Risk Students:", no_risk)

print("\nAcademic Risk Analysis Completed.")

