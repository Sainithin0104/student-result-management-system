while True:
    print("\n========== Student Result Management System ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file = open("students.txt", "a")

        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        marks = int(input("Enter Marks: "))

        file.write(name + "," + roll + "," + str(marks) + "\n")
        file.close()

        print("Student Added Successfully!")

    elif choice == "2":
        try:
            file = open("students.txt", "r")

            print("\n------ Student Records ------")

            for line in file:
                data = line.strip().split(",")
                print("Name :", data[0])
                print("Roll :", data[1])
                print("Marks:", data[2])
                print("----------------------------")

            file.close()

        except FileNotFoundError:
            print("No student records found!")

    elif choice == "3":
        try:
            file = open("students.txt", "r")

            search_roll = input("Enter Roll Number to Search: ")
            found = False

            for line in file:
                data = line.strip().split(",")

                if data[1] == search_roll:
                    print("\nStudent Found")
                    print("Name :", data[0])
                    print("Roll :", data[1])
                    print("Marks:", data[2])
                    found = True
                    break

            if not found:
                print("Student Not Found")

            file.close()

        except FileNotFoundError:
            print("No student records found!")

    elif choice == "4":
        try:
            file = open("students.txt", "r")

            topper_name = ""
            topper_roll = ""
            highest_marks = -1

            for line in file:
                data = line.strip().split(",")

                name = data[0]
                roll = data[1]
                marks = int(data[2])

                if marks > highest_marks:
                    highest_marks = marks
                    topper_name = name
                    topper_roll = roll

            file.close()

            if highest_marks == -1:
                print("No student records found!")
            else:
                print("\n------ Class Topper ------")
                print("Name :", topper_name)
                print("Roll :", topper_roll)
                print("Marks:", highest_marks)

        except FileNotFoundError:
            print("No student records found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
