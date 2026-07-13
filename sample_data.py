from person import Student, Teacher, Admin, Principal
from database import students, teachers, admins
import database

# ===================== STUDENTS =====================

student1 = Student(
    "S501",
    "Rahul Sharma",
    20,
    "Male",
    "9876543210",
    "r",
    "BCA",
    3
)

student1.subject_marks = {
    "Python": 85,
    "Java": 90,
    "DBMS": 88,
    "OS": 80,
    "CN": 92
}

student1.attendance["present"] = 42
student1.attendance["total_classes"] = 50


student2 = Student(
    "S502",
    "Priya Singh",
    21,
    "Female",
    "9123456789",
    "priya123",
    "BCA",
    3
)

student2.subject_marks = {
    "Python": 95,
    "Java": 91,
    "DBMS": 89,
    "OS": 94,
    "CN": 90
}

student2.attendance["present"] = 48
student2.attendance["total_classes"] = 50


students[student1.person_id] = student1
students[student2.person_id] = student2


# ===================== TEACHERS =====================

teacher1 = Teacher(
    "T51",
    "Amit Kumar",
    35,
    "Male",
    "9988776655",
    "a",
    "Python",
    50000
)

teacher2 = Teacher(
    "T52",
    "Neha Verma",
    32,
    "Female",
    "9876501234",
    "neha123",
    "Java",
    55000
)

teachers[teacher1.person_id] = teacher1
teachers[teacher2.person_id] = teacher2


# ===================== ADMINS =====================

admin1 = Admin(
    "A1",
    "Suraj Sharma",
    23,
    "Male",
    "9876543201",
    "s"
)

admins[admin1.person_id] = admin1


# ===================== PRINCIPAL =====================

database.principal = Principal(
    "P0",
    "Dr. Rajesh Sharma",
    55,
    "Male",
    "9876543299",
    "p"
)