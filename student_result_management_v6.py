# Student Result Management System - Version 6

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = ["Python", "Maths", "English", "Science", "Social"]
marks = []

total = 0

for subject in subjects:
    mark = int(input(f"Enter {subject} Marks: "))
    marks.append(mark)
    total += mark

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

# Overall Result
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

# Display Result
print("\n========== STUDENT RESULT ==========")
print("Name           :", name)
print("Roll Number    :", roll_no)

for i in range(len(subjects)):
    if marks[i] >= 35:
        status = "Pass"
    else:
        status = "Fail"

    print(f"{subjects[i]:15}: {marks[i]} ({status})")

print("------------------------------------")
print("Total          :", total)
print("Percentage     :", round(percentage, 2), "%")
print("Grade          :", grade)
print("Rank           :", rank)
print("Top Subject    :", top_subject)
print("Highest Mark   :", highest)
print("Lowest Mark    :", lowest)
print("Overall Result :", result)
print("Remarks        :", remarks)
