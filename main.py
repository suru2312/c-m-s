#================================ IMPORTS ====================================
import os

# import sample_data
from file_handler import load_all, save_all

import database

from database import students, teachers, admins
from person import Person, Student, Teacher, Admin, Principal
from college import College
from exceptions import (
    InvalidAgeError, 
    InvalidMobileError,
    InvalidAttendanceError,
    InvalidSubjectMarksError,
    InvalidInput
)

college = College("Bridgefix College Management System")

#================================ METHODS ====================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    clear_screen()
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)

def welcome_screen():
    print_header(college.name)

def pause():
    input("\nPress ENTER to Continue...")

def login():
    load_all()
    print_header("LOGIN PAGE")
    print("[Enter 'QUIT' for Exiting the program.]".center(60))
    person_id = input("Enter ID         : ").strip().upper()
    if not person_id == "QUIT":
        password = input("Enter Password   : ").strip()
        if not person_id:
            raise InvalidInput("ID cannot be empty.")
        if not password:
            raise InvalidInput("Password cannot be empty.")
        return authenticate(person_id, password)
    else:
        return "EXIT-101"

def authenticate(person_id, password):
    person_id = person_id.strip().upper()
    password = password.strip()
    if person_id.startswith("S"):
        student = students.get(person_id)
        if student is not None:
            if student.verify_login(person_id, password):
                return student
    elif person_id.startswith("T"):
        teacher = teachers.get(person_id)
        if teacher:
            if teacher.verify_login(person_id, password):
                return teacher
    elif person_id.startswith("A"):
        admin = admins.get(person_id)
        if admin:
            if admin.verify_login(person_id, password):
                return admin
    elif person_id == "P0":
        if database.principal and database.principal.verify_login(person_id, password):
            return database.principal
    return None

def get_student():
    student_id = input("Enter Student ID : ").strip().upper()
    if not student_id:
        raise InvalidInput("Student ID cannot be empty.")
    student = students.get(student_id)
    if not student:
        print("\nStudent Not Found!")
    return student

#================================ STUDENT DASHBOARD ==========================

def student_dashboard(student):
    while True:
        print_header("STUDENT DASHBOARD")
        print(f"\nWelcome {student.name}")
        print()
        print("1. View Result")
        print("2. View Attendance")
        print("3. Pay Fee")
        print("4. Change password")
        print("5. View Classroom")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. Logout")
        print()
        user_choice = input("Enter Choice : ")
        if user_choice == "1":
            student.view_result()
            pause()
        elif user_choice == "2":
            try:
                present, absent, total, percentage = student.calculate_attendance()
                print("\n" + "=" * 50)
                print("ATTENDANCE".center(50))
                print("=" * 50)
                print(f"Present Classes : {present}")
                print(f"Absent Classes  : {absent}")
                print(f"Total Classes   : {total}")
                print(f"Attendance      : {percentage}%")
            except InvalidAttendanceError as e:
                print(e)
            pause()
        elif user_choice == "3":
            student.pay_fee()
            pause()
        elif user_choice == "4":
            print()
            old_password = input("Enter Old Password : ")
            new_password = input("Enter New Password : ")
            try:
                student.change_password(old_password, new_password)
            except InvalidInput as e:
                print(e)
            pause()
        elif user_choice == "5":
            college.classroom.view_classroom(student)
            pause()
        elif user_choice == "6":
            print()
            book = input("Enter Book Name : ")
            college.library.issue_book(student, book)
            pause()
        elif user_choice == "7":
            print()
            book = input("Enter Book Name : ")
            college.library.return_book(student, book)
            pause()
        elif user_choice == "8":
            student.logout()
            pause()
            break
        else:
            print("Enter a valid Input!")
            pause()

#================================ TEACHER DASHBOARD ==========================

def teacher_dashboard(teacher):
    while True:
        print_header("TEACHER DASHBOARD")
        print(f"\nWelcome {teacher.name}")
        print()
        print("1. Add Marks")
        print("2. Update Marks")
        print("3. Take Attendance")
        print("4. Change password")
        print("5. View Classrooms")
        print("6. Logout")
        print()
        user_choice = input("Enter Choice : ")
        if user_choice == "1":
            print()
            student = get_student()
            if student:
                try:
                    teacher.add_marks(student)
                except (InvalidSubjectMarksError, InvalidInput) as e:
                    print(e)
            pause()
        elif user_choice == "2":
            print()
            student = get_student()
            if student:
                try:
                    teacher.update_marks(student)
                except (InvalidSubjectMarksError, InvalidInput) as e:
                    print(e)
            pause()
        elif user_choice == "3":
            print()
            student = get_student()
            if student:
                try:
                    teacher.take_attendance(student)
                except InvalidInput as e:
                    print(e)
            pause()
        elif user_choice == "4":
            print()
            old_password = input("Enter Old Password : ")
            new_password = input("Enter New Password : ")
            try:
                teacher.change_password(old_password, new_password)
            except InvalidInput as e:
                print(e)
            pause()
        elif user_choice == "5":
            college.classroom.display_rooms()
            pause()
        elif user_choice == "6":
            teacher.logout()
            pause()
            break
        else:
            print("\nInvalid Input!")
            pause()

#================================ ADMIN DASHBOARD ============================

def admin_dashboard(admin):
    while True:
        print_header("ADMIN DASHBOARD")
        print(f"\nWelcome {admin.name}\n")
        print()
        print("1. Add Student            2. Update Student")
        print("3. Delete Student         4. Search Student")
        print("5. View Students          6. Add Teacher")
        print("7. Update Teacher         8. Delete Teacher")
        print("9. View Teachers          10. Change Password")
        print("               11. Logout")
        print()
        user_choice = input("Enter Choice : ")
        print()
        if user_choice == "1":
            try:
                admin.add_student(students)
            except (InvalidAgeError, InvalidMobileError, InvalidInput) as e:
                print(e)
            pause()
        elif user_choice == "2":
            try:
                admin.update_student(students)
            except (InvalidInput, InvalidMobileError) as e:
                print(e)
            pause()
        elif user_choice == "3":
            admin.delete_student(students)
            pause()
        elif user_choice == "4":
            try:
                admin.search_student(students)
            except InvalidInput as e:
                print(e)
            pause()
        elif user_choice == "5":
            admin.view_students(students)
            pause()
        elif user_choice == "6":
            try:
                admin.add_teacher(teachers)
            except (InvalidAgeError, InvalidMobileError, InvalidInput) as e:
                print(e)
            pause()
        elif user_choice == "7":
            try:
                admin.update_teacher(teachers)
            except (InvalidInput, InvalidMobileError) as e:
                print(e)
            pause()
        elif user_choice == "8":
            admin.delete_teacher(teachers)
            pause()
        elif user_choice == "9":
            admin.view_teachers(teachers)
            pause()
        elif user_choice == "10":
            print()
            old_password = input("Enter Old Password : ")
            new_password = input("Enter New Password : ")
            try:
                admin.change_password(old_password, new_password)
            except InvalidInput as e:
                print(e)
            pause()
        elif user_choice == "11":
            admin.logout()
            pause()
            break
        else:
            print("\nInvalid Choice!")
            pause()

#================================ PRINCIPAL DASHBOARD ========================

def principal_dashboard(principal):
    while True:
        print_header("PRINCIPAL DASHBOARD")
        print(f"\nWelcome {principal.name}")
        print()
        print("1. Top 3 Students            2. Highest Percentage")
        print("3. Average Percentage        4. Pass/Fail Report")
        print("5. Highest Attendance        6. Average Attendance")
        print("7. Pending Fee Students      8. College Summary")
        print("9. Change Password           10. Update Profile")
        print("11. Create Admin             12. Logout")
        print()
        user_choice = input("Enter Choice : ")
        if user_choice == "1":
            principal.top_three_students(students)
            pause()
        elif user_choice == "2":
            principal.highest_percentage(students)
            pause()
        elif user_choice == "3":
            principal.average_percentage(students)
            pause()
        elif user_choice == "4":
            principal.pass_fail_report(students)
            pause()
        elif user_choice == "5":
            try:
                principal.highest_attendance(students)
            except InvalidAttendanceError as e:
                print(e)
            pause()
        elif user_choice == "6":
            try:
                principal.average_attendance(students)
            except InvalidAttendanceError as e:
                print(e)
            pause()
        elif user_choice == "7":
            principal.pending_fee_students(students)
            pause()
        elif user_choice == "8":
            principal.college_summary(students, teachers, admins)
            print("=" * 50)
            pause()
        elif user_choice == "9":
            print()
            old_password = input("Enter Old Password : ")
            new_password = input("Enter New Password : ")
            try:
                principal.change_password(old_password, new_password)
            except InvalidInput as e:
                print(e)
            pause()
        elif user_choice == "10":
            principal.update_profile()
            save_all()
            pause()
        elif user_choice == "11":
            principal.create_admin(admins)
            save_all()
            pause()
        elif user_choice == "12":
            principal.logout()
            pause()
            break
        else:
            print("\nInvalid Choice!")
            pause()

#================================ MAIN =======================================

def main():

    load_all()
    
    while True:
        welcome_screen()
        load_all()
        try:
            user = login()
            if user == "EXIT-101":
                os.system("clear")
                print("=" * 60)
                print("THANKYOU!".center(60))
                print("=" * 60)
                save_all()
                break
        except InvalidInput as e:
            print(e)
            pause()
            continue

        if user is not None:
            if isinstance(user, Student):
                student_dashboard(user)

            elif isinstance(user, Teacher):
                teacher_dashboard(user)

            elif isinstance(user, Admin):
                admin_dashboard(user)

            elif isinstance(user, Principal):
                principal_dashboard(user)
        else:
            print("\nInvalid ID or Password!")
            pause()
        
        save_all()

main()