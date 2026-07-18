## Student Result Management System - Version 4

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

# Subject-wise Pass/Fail
print("\n----- Subject Result -----")

if python >= 35:
    print("Python  : Pass")
else:
    print("Python  : Fail")

if maths >= 35:
    print("Maths   : Pass")
else:
    print("Maths   : Fail")

if english >= 35:
    print("English : Pass")
else:
    print("English : Fail")

# Overall Result
if python >= 35 and maths >= 35 and english >= 35:
    result = "Pass"
else:
    result = "Fail"

# Display Result
print("\n----- Student Result -----")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Overall Result :", result)
