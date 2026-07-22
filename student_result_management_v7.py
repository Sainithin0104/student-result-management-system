students = []

while True:
    print("\n===== Student Result Management System =====")

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    subjects = ["Python", "Maths", "English", "Science", "Social"]
    marks = []

    total = 0
    passed_subjects = 0

    for subject in subjects:
        mark = int(input(f"Enter {subject} Marks: "))
        marks.append(mark)
        total += mark

        if mark >= 35:
            passed_subjects += 1

    percentage = total / len(subjects)

    # Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Rank
    if percentage >= 90:
        rank = "Excellent"
    elif percentage >= 80:
        rank = "Very Good"
    elif percentage >= 70:
        rank = "Good"
    elif percentage >= 60:
        rank = "Average"
    else:
        rank = "Needs Improvement"

    # Highest, Lowest and Top Subject
    highest = marks[0]
    lowest = marks[0]
    top_subject = subjects[0]

    for i in range(len(marks)):
        if marks[i] > highest:
            highest = marks[i]
            top_subject = subjects[i]

        if marks[i] < lowest:
            lowest = marks[i]

    # Result
    result = "PASS"

    for mark in marks:
        if mark < 35:
            result = "FAIL"
            break

    # Remarks
    if result == "FAIL":
        remarks = "Better Luck Next Time"
    elif percentage >= 75:
        remarks = "Outstanding Performance"
    elif percentage >= 60:
        remarks = "Good Performance"
    else:
        remarks = "Needs Improvement"

    # Store Student Data
    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "rank": rank,
        "result": result,
        "remarks": remarks,
        "top_subject": top_subject,
        "highest": highest,
        "lowest": lowest
    }

    students.append(student)

    choice = input("\nDo you want to enter another student? (yes/no): ")

    if choice.lower() == "no":
        break

# Class Report
total_students = len(students)
passed = 0
failed = 0

for student in students:
    if student["result"] == "PASS":
        passed += 1
    else:
        failed += 1

pass_percentage = (passed / total_students) * 100

print("\n========== CLASS REPORT ==========")
print("Total Students :", total_students)
print("Passed         :", passed)
print("Failed         :", failed)
print("Pass Percentage:", round(pass_percentage, 2), "%")

# Search Student
while True:
    search = input("\nEnter Roll Number to Search: ")

    found = False

    for student in students:
        if student["roll"] == search:
            found = True

            print("\n===== STUDENT DETAILS =====")
            print("Name :", student["name"])
            print("Roll :", student["roll"])

            subjects = ["Python", "Maths", "English", "Science", "Social"]

            for i in range(len(subjects)):
                print(subjects[i], ":", student["marks"][i])

            print("Total :", student["total"])
            print("Percentage :", round(student["percentage"], 2))
            print("Grade :", student["grade"])
            print("Rank :", student["rank"])
            print("Top Subject :", student["top_subject"])
            print("Highest Mark :", student["highest"])
            print("Lowest Mark :", student["lowest"])
            print("Result :", student["result"])
            print("Remarks :", student["remarks"])

            break

    if not found:
        print("Student Not Found!")

    again = input("\nSearch another student? (yes/no): ")

    if again.lower() == "no":
        break
