#============================== IMPORTS ==============================

from person import Student, Teacher, Admin, Principal
from database import students, teachers, admins
import database

def save_students():
    with open("students.txt", "w") as file:
        for student in students.values():
            file.write(
                f"{student.person_id},"
                f"{student.name},"
                f"{student.age},"
                f"{student.gender},"
                f"{student.mobile},"
                f"{student.password},"
                f"{student.course},"
                f"{student.semester}\n"
            )

