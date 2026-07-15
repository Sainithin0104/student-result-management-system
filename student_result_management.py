# Student Result Management System - Version 2

# Get student details
name = input("Enter Student Name: ")

python = int(input("Enter Python Marks: "))
maths = int(input("Enter Maths Marks: "))
english = int(input("Enter English Marks: "))

# Calculate total and percentage
total = python + maths + english
percentage = total / 3

# Calculate grade
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

# Pass or Fail
if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

# Display result
print("\n========== STUDENT RESULT ==========")
print("Student Name :", name)
print("Python Marks :", python)
print("Maths Marks  :", maths)
print("English Marks:", english)
print("------------------------------------")
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Result       :", result)
print("====================================")
