
# University Examination Result Moderation

print("======================================")
print(" UNIVERSITY EXAMINATION RESULT")
print("          MODERATION SYSTEM")
print("======================================")

student_name = input("Enter Student Name: ")
n = int(input("Enter Number of Subjects: "))

pass_mark = 40
moderation = 5

subjects = []
original_marks = []
moderated_marks = []

# Input subject details
for i in range(n):
    print("\nSubject", i + 1)

    subject = input("Enter Subject Name: ")
    marks = int(input("Enter Original Marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    # Apply moderation
    if 35 <= marks < pass_mark:
        new_marks = min(marks + moderation, 100)
    else:
        new_marks = marks

    subjects.append(subject)
    original_marks.append(marks)
    moderated_marks.append(new_marks)

# Calculate totals
original_total = sum(original_marks)
moderated_total = sum(moderated_marks)

# Calculate percentages
original_percentage = original_total / n
moderated_percentage = moderated_total / n

# Check pass/fail status
original_result = all(
    mark >= pass_mark for mark in original_marks
)

moderated_result = all(
    mark >= pass_mark for mark in moderated_marks
)

# Display result
print("\n======================================")
print("       EXAMINATION RESULT REPORT")
print("======================================")

print("Student Name:", student_name)

print("\nSubject-wise Marks")
print("--------------------------------------")
print("Subject       Original   Moderated")
print("--------------------------------------")

for i in range(n):
    print(f"{subjects[i]:<14}{original_marks[i]:<11}"
          f"{moderated_marks[i]}")

print("--------------------------------------")
print("Original Total:", original_total)
print("Moderated Total:", moderated_total)

print("Original Percentage:",
      round(original_percentage, 2), "%")

print("Moderated Percentage:",
      round(moderated_percentage, 2), "%")

print("Marks Improved:",
      moderated_total - original_total)

print("\nOriginal Result:",
      "PASS" if original_result else "FAIL")

print("Moderated Result:",
      "PASS" if moderated_result else "FAIL")

print("\n======================================")
print("          END OF REPORT")
print("======================================")

