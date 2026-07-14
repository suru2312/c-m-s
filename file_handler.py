#============================== IMPORTS ==============================

import os
import json
from person import Student, Teacher, Admin, Principal
from database import students, teachers, admins
import database

#============================== METHODS ==============================

def save_students():
    data = []
    for student in students.values():
        student_data = {
            "person_id": student.person_id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender,
            "mobile": student.mobile,
            "password": student.password,
            "course": student.course,
            "semester": student.semester,
            "subject_marks": student.subject_marks,
            "attendance": student.attendance,
            "fee": student.fee
        }
        data.append(student_data)
    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_students():
    if not os.path.exists("students.json"):
        return
    students.clear()
    Student.total_students = 0
    try:
        with open("students.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("students.json is corrupted.")
        return
    for item in data:
        student = Student(
            item["person_id"],
            item["name"],
            item["age"],
            item["gender"],
            item["mobile"],
            item["password"],
            item["course"],
            item["semester"]
        )
        if item["subject_marks"]:
            student.subject_marks = item["subject_marks"]
        student.attendance = item["attendance"]
        student.fee = item["fee"]
        students[student.person_id] = student

def save_teachers():
    data = []
    for teacher in teachers.values():
        teacher_data = {
            "person_id": teacher.person_id,
            "name": teacher.name,
            "age": teacher.age,
            "gender": teacher.gender,
            "mobile": teacher.mobile,
            "password": teacher.password,
            "subject": teacher.subject,
            "salary": teacher.salary
        }
        data.append(teacher_data)
    with open("teachers.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_teachers():
    if not os.path.exists("teachers.json"):
        return
    teachers.clear()
    Teacher.total_teachers = 0
    try: 
        with open("teachers.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("teachers.json is corrupted.")
        return
    for item in data:
        teacher = Teacher(
            item["person_id"],
            item["name"],
            item["age"],
            item["gender"],
            item["mobile"],
            item["password"],
            item["subject"],
            item["salary"]
        )
        teachers[teacher.person_id] = teacher

def save_admins():
    data = []
    for admin in admins.values():
        admin_data = {
            "person_id": admin.person_id,
            "name": admin.name,
            "age": admin.age,
            "gender": admin.gender,
            "mobile": admin.mobile,
            "password": admin.password
        }
        data.append(admin_data)
    with open("admins.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_admins():
    if not os.path.exists("admins.json"):
        return
    admins.clear()
    Admin.total_admin = 0
    try:
        with open("admins.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("admins.json is corrupted.")
        return
    for item in data:
        admin = Admin(
            item["person_id"],
            item["name"],
            item["age"],
            item["gender"],
            item["mobile"],
            item["password"]
        )
        admins[admin.person_id] = admin

def save_principal():
    if database.principal is None:
        return
    data = {
        "person_id": database.principal.person_id,
        "name": database.principal.name,
        "age": database.principal.age,
        "gender": database.principal.gender,
        "mobile": database.principal.mobile,
        "password": database.principal.password
    }
    with open("principal.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_principal():
    if not os.path.exists("principal.json"):
        return
    try:
        with open("principal.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("principal.json is corrupted.")
        return
    database.principal = Principal(
        data["person_id"],
        data["name"],
        data["age"],
        data["gender"],
        data["mobile"],
        data["password"]
    )

def save_all():
    save_students()
    save_teachers()
    save_admins()
    save_principal()

def load_all():

    # ===================== STUDENTS =====================

    if os.path.exists("students.json"):
        load_students()
    else:
        print("\nstudents.json not found. Creating new file...")
        save_students()

    # ===================== TEACHERS =====================

    if os.path.exists("teachers.json"):
        load_teachers()
    else:
        print("\nteachers.json not found. Creating new file...")
        save_teachers()

    # ===================== ADMINS =====================

    if os.path.exists("admins.json"):
        load_admins()
    else:
        print("\nadmins.json not found. Creating new file...")
        save_admins()

    # ===================== PRINCIPAL =====================

    if os.path.exists("principal.json"):
        load_principal()
    else:
        print("\nprincipal.json not found. Creating System Principal...")
        database.principal = Principal(
            "P0",
            "System Principal",
            50,
            "Male",
            "9999999998",
            "admin123"
        )
        save_principal()