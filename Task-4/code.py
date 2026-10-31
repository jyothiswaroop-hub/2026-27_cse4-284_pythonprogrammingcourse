
# COMPREHENSIVE SMART CAMPUS MANAGEMENT SYSTEM

students = []
attendance = []
marks = []
events = []
resources = []

# Function to check student existence
def student_exists(sid):
    for student in students:
        if student[0] == sid:
            return True
    return False


# Function to add student records
def add_student():
    sid = input("Enter Student ID: ")

    if student_exists(sid):
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    year = input("Enter Year: ")

    students.append([sid, name, dept, year])
    print("Student added successfully!")


# Function to record attendance
def record_attendance():
    sid = input("Enter Student ID: ")

    if not student_exists(sid):
        print("Student not found!")
        return

    total = int(input("Enter Total Classes: "))
    attended = int(input("Enter Attended Classes: "))

    if total <= 0 or attended < 0 or attended > total:
        print("Invalid attendance details!")
        return

    percentage = (attended / total) * 100

    attendance.append([sid, total, attended, percentage])

    print("Attendance recorded successfully!")
    print("Attendance Percentage:", round(percentage, 2), "%")


# Function to enter marks
def enter_marks():
    sid = input("Enter Student ID: ")

    if not student_exists(sid):
        print("Student not found!")
        return

    subject_marks = []

    for i in range(1, 4):
        mark = float(input(f"Enter Subject {i} Marks: "))

        if mark < 0 or mark > 100:
            print("Invalid mark! Enter between 0 and 100.")
            return

        subject_marks.append(mark)

    total = sum(subject_marks)
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    marks.append([sid, subject_marks, total, average, grade])

    print("Marks recorded successfully!")
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


# Function for event registration
def register_event():
    sid = input("Enter Student ID: ")

    if not student_exists(sid):
        print("Student not found!")
        return

    event_name = input("Enter Event Name: ")

    # Tuple storing registration details
    registration = (sid, event_name)
    events.append(registration)

    print("Event registration successful!")


# Function for resource allocation
def allocate_resource():
    resource_name = input("Enter Resource Name: ")
    quantity = int(input("Enter Quantity: "))
    location = input("Enter Location: ")

    if quantity <= 0:
        print("Invalid quantity!")
        return

    # Tuple storing resource information
    allocation = (resource_name, quantity, location)
    resources.append(allocation)

    print("Resource allocated successfully!")


# Function to display summary report
def summary_report():
    print("\n========== SMART CAMPUS REPORT ==========")

    print("\n--- STUDENT RECORDS ---")

    for sid, name, dept, year in students:
        print("ID:", sid, "| Name:", name,
              "| Department:", dept, "| Year:", year)

    print("\n--- ATTENDANCE REPORT ---")

    for sid, total, attended, percentage in attendance:
        print("Student ID:", sid)
        print("Total Classes:", total)
        print("Attended Classes:", attended)
        print("Percentage:", round(percentage, 2), "%")

    print("\n--- MARKS REPORT ---")

    for sid, subject_marks, total, average, grade in marks:
        print("Student ID:", sid)
        print("Subject Marks:", subject_marks)
        print("Total:", total)
        print("Average:", round(average, 2))
        print("Grade:", grade)

    print("\n--- EVENT REGISTRATIONS ---")

    for sid, event_name in events:
        print("Student ID:", sid, "| Event:", event_name)

    print("\n--- RESOURCE ALLOCATION ---")

    for resource_name, quantity, location in resources:
        print("Resource:", resource_name)
        print("Quantity:", quantity)
        print("Location:", location)

    print("\n========== END OF REPORT ==========")


# Main menu
while True:

    print("\n===== SMART CAMPUS MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Record Attendance")
    print("3. Enter Marks")
    print("4. Register for Event")
    print("5. Allocate Resources")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        record_attendance()

    elif choice == "3":
        enter_marks()

    elif choice == "4":
        register_event()

    elif choice == "5":
        allocate_resource()

    elif choice == "6":
        summary_report()

    elif choice == "7":
        print("Thank you for using Smart Campus Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

