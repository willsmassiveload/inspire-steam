#Name : William Karanja
# Date : 23/02/2026
# Program to show students module in

name = "John Kangethe"

fav_sport = "Tennis"

height = 1.2


def show_details(name,height,fav_sport):
    print(f" {name} is {height} metres tal a enjoys playing {fav_sport}")
# student.py

class Student:
    def __init__(self, student_id, name, course, phone):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.phone = phone
        self.grade = None

    def assign_course_grade(self, new_course, grade):
        self.course = new_course
        self.grade = grade

    def display(self):
        return [self.student_id, self.name, self.course, self.phone, self.grade]