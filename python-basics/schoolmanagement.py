# program to register students
import openpyxl

students = []

def register_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")

    student = Student(student_id, name, course, phone)
    students.append(student)
    print("Student Registered Successfully!\n")


def display_students():
    if not students:
        print("No students registered.\n")
        return

    for s in students:
        print(s.display())
    print()


def assign_course_grade():
    student_id = input("Enter Student ID: ")
    for s in students:
        if s.student_id == student_id:
            new_course = input("Enter New Course: ")
            grade = input("Enter Grade: ")
            s.assign_course_grade(new_course, grade)
            print("Updated Successfully!\n")
            return
    print("Student Not Found!\n")


def save_to_excel():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["ID", "Name", "Course", "Phone", "Grade"])

    for s in students:
        sheet.append(s.display())

    workbook.save("students.xlsx")
    print("Saved to Excel Successfully!\n")


while True:
    print("===== SCHOOL MANAGEMENT SYSTEM =====")
    print("1. Register Student")
    print("2. Display Students")
    print("3. Assign Course & Grade")
    print("4. Save to Excel")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        assign_course_grade()
    elif choice == "4":
        save_to_excel()
    elif choice == "5":
        break
    else:
        print("Invalid Choice\n")