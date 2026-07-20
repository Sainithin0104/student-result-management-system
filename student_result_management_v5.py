# Student Result Management System - Version 5

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

# Highest and Lowest (without max() and min())
highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

# Overall Result
result = "PASS"

print("\n------ Student Result ------")
print("Name      :", name)
print("Roll No   :", roll_no)

for i in range(len(subjects)):
    if marks[i] >= 35:
        status = "Pass"
    else:
        status = "Fail"
        result = "FAIL"

    print(f"{subjects[i]} : {marks[i]} ({status})")

print("\nTotal       :", total)
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)
print("Highest Mark:", highest)
print("Lowest Mark :", lowest)
print("Overall Result:", result)
