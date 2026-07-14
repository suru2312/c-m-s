# from person import Student, Teacher, Admin, Principal
# from database import students, teachers, admins
# import database

# # ===================== STUDENTS =====================

# student1 = Student(
#     "S501",
#     "Rahul Sharma",
#     20,
#     "Male",
#     "9876543210",
#     "rahul123",
#     "BCA",
#     3
# )
# student1.subject_marks = {
#     "Python": 85,
#     "Java": 90,
#     "DBMS": 88,
#     "OS": 80,
#     "CN": 92
# }
# student1.attendance["present"] = 42
# student1.attendance["total_classes"] = 50
# student1.fee["paid"] = True


# student2 = Student(
#     "S502",
#     "Priya Singh",
#     21,
#     "Female",
#     "9123456789",
#     "priya123",
#     "BCA",
#     3
# )
# student2.subject_marks = {
#     "Python": 95,
#     "Java": 91,
#     "DBMS": 89,
#     "OS": 94,
#     "CN": 90
# }
# student2.attendance["present"] = 48
# student2.attendance["total_classes"] = 50
# student2.fee["paid"] = False


# student3 = Student(
#     "S503",
#     "Aman Verma",
#     19,
#     "Male",
#     "9988776655",
#     "aman123",
#     "BTECH",
#     2
# )
# student3.subject_marks = {
#     "Python": 72,
#     "Java": 68,
#     "DBMS": 75,
#     "OS": 70,
#     "CN": 74
# }
# student3.attendance["present"] = 44
# student3.attendance["total_classes"] = 50
# student3.fee["paid"] = True


# student4 = Student(
#     "S504",
#     "Neha Gupta",
#     22,
#     "Female",
#     "9876501234",
#     "neha123",
#     "MCA",
#     1
# )
# student4.subject_marks = {
#     "Python": 98,
#     "Java": 96,
#     "DBMS": 95,
#     "OS": 97,
#     "CN": 99
# }
# student4.attendance["present"] = 50
# student4.attendance["total_classes"] = 50
# student4.fee["paid"] = True


# student5 = Student(
#     "S505",
#     "Rohit Kumar",
#     20,
#     "Male",
#     "9765432109",
#     "rohit123",
#     "BBA",
#     4
# )
# student5.subject_marks = {
#     "Python": 55,
#     "Java": 60,
#     "DBMS": 58,
#     "OS": 62,
#     "CN": 57
# }
# student5.attendance["present"] = 35
# student5.attendance["total_classes"] = 50
# student5.fee["paid"] = False


# student6 = Student(
#     "S506",
#     "Sneha Patel",
#     21,
#     "Female",
#     "9654321098",
#     "sneha123",
#     "MBA",
#     2
# )
# student6.subject_marks = {
#     "Python": 81,
#     "Java": 79,
#     "DBMS": 84,
#     "OS": 80,
#     "CN": 83
# }
# student6.attendance["present"] = 46
# student6.attendance["total_classes"] = 50
# student6.fee["paid"] = True


# student7 = Student(
#     "S507",
#     "Vikas Yadav",
#     23,
#     "Male",
#     "9543210987",
#     "vikas123",
#     "MSC",
#     3
# )
# student7.subject_marks = {
#     "Python": 42,
#     "Java": 38,
#     "DBMS": 45,
#     "OS": 40,
#     "CN": 41
# }
# student7.attendance["present"] = 28
# student7.attendance["total_classes"] = 50
# student7.fee["paid"] = False


# student8 = Student(
#     "S508",
#     "Pooja Mishra",
#     20,
#     "Female",
#     "9432109876",
#     "pooja123",
#     "BSC",
#     5
# )
# student8.subject_marks = {
#     "Python": 88,
#     "Java": 86,
#     "DBMS": 90,
#     "OS": 91,
#     "CN": 89
# }
# student8.attendance["present"] = 47
# student8.attendance["total_classes"] = 50
# student8.fee["paid"] = True


# student9 = Student(
#     "S509",
#     "Arjun Mehta",
#     22,
#     "Male",
#     "9321098765",
#     "arjun123",
#     "MTECH",
#     2
# )
# student9.subject_marks = {
#     "Python": 67,
#     "Java": 71,
#     "DBMS": 69,
#     "OS": 73,
#     "CN": 70
# }
# student9.attendance["present"] = 40
# student9.attendance["total_classes"] = 50
# student9.fee["paid"] = True


# student10 = Student(
#     "S510",
#     "Kavya Joshi",
#     19,
#     "Female",
#     "9210987654",
#     "kavya123",
#     "BCA",
#     1
# )
# student10.subject_marks = {
#     "Python": 76,
#     "Java": 82,
#     "DBMS": 79,
#     "OS": 81,
#     "CN": 78
# }
# student10.attendance["present"] = 43
# student10.attendance["total_classes"] = 50
# student10.fee["paid"] = False


# students[student1.person_id] = student1
# students[student2.person_id] = student2
# students[student3.person_id] = student3
# students[student4.person_id] = student4
# students[student5.person_id] = student5
# students[student6.person_id] = student6
# students[student7.person_id] = student7
# students[student8.person_id] = student8
# students[student9.person_id] = student9
# students[student10.person_id] = student10

# # ===================== TEACHERS =====================

# teacher1 = Teacher(
#     "T51",
#     "Amit Kumar",
#     35,
#     "Male",
#     "9988776655",
#     "amit123",
#     "Python",
#     50000
# )

# teacher2 = Teacher(
#     "T52",
#     "Neha Verma",
#     32,
#     "Female",
#     "9876501234",
#     "neha123",
#     "Java",
#     55000
# )

# teacher3 = Teacher(
#     "T53",
#     "Rajesh Singh",
#     40,
#     "Male",
#     "9765432109",
#     "rajesh123",
#     "Database Management",
#     62000
# )

# teacher4 = Teacher(
#     "T54",
#     "Pooja Sharma",
#     29,
#     "Female",
#     "9654321098",
#     "pooja123",
#     "Operating Systems",
#     48000
# )

# teacher5 = Teacher(
#     "T55",
#     "Vikram Patel",
#     38,
#     "Male",
#     "9543210987",
#     "vikram123",
#     "Computer Networks",
#     60000
# )

# teachers[teacher1.person_id] = teacher1
# teachers[teacher2.person_id] = teacher2
# teachers[teacher3.person_id] = teacher3
# teachers[teacher4.person_id] = teacher4
# teachers[teacher5.person_id] = teacher5

# # ===================== ADMINS =====================

# admin1 = Admin(
#     "A1",
#     "Suraj Sharma",
#     23,
#     "Male",
#     "9876543201",
#     "admin123"
# )

# admin2 = Admin(
#     "A2",
#     "Anjali Verma",
#     30,
#     "Female",
#     "9876543202",
#     "anjali123"
# )

# admins[admin1.person_id] = admin1
# admins[admin2.person_id] = admin2


# # ===================== PRINCIPAL =====================

# database.principal = Principal(
#     "P0",
#     "Dr. Rajesh Sharma",
#     55,
#     "Male",
#     "9876543299",
#     "principal123"
# )