class Student:
    def __init__(self, student_id, name, course, phone):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.phone = phone
        self.grade = None

    def assign_grade(self, grade):
        self.grade = grade