#======================================= IMPORTS ======================================

from prettytable import PrettyTable
from exceptions import (
    InvalidAgeError, 
    InvalidMobileError,
    InvalidAttendanceError,
    InvalidSubjectMarksError,
    InvalidInput
)

#====================================== CONSTANTS ======================================

MIN_MARKS = 0
MAX_MARKS = 100
MIN_AGE = 18
MAX_AGE = 100
MAX_ATTENDANCE = 100
MIN_ATTENDANCE = 0
VALID_GENDERS = ("Male", "Female", "Other")
MIN_SEMESTER = 1
MAX_SEMESTER = 8
VALID_COURSES = {"BBA", "MTECH", "BCA", "BTECH", "MCA", "MBA", "BSC", "MSC"}

#======================================== PERSON =======================================

class Person:

    #---------------------- CONSTRUCTOR ---------------------------
    
    def __init__(self, person_id, name, age, gender, mobile, password):
        
        self.person_id = person_id
        
        if len(name.strip()) < 3:
            raise InvalidInput("Name must contain at least 3 characters.")
        if not all(ch.isalpha() or ch.isspace() for ch in name):
            raise InvalidInput("Name can contain only alphabets and spaces.")
        self.name = name.strip().title()
        
        if not (MIN_AGE <= age <= MAX_AGE):
            raise InvalidAgeError(f"Age must be between {MIN_AGE} and {MAX_AGE}.")
        self.age = age
        
        gender = gender.strip().title()
        if gender not in VALID_GENDERS:
            raise InvalidInput(
                f"Gender must be one of {', '.join(VALID_GENDERS)}."
            )
        self.gender = gender
        
        if not Person.validate_mobile(mobile):
            raise InvalidMobileError("Invalid Mobile Number.")
        self.mobile = mobile
        
        password = password.strip()
        if not password:
            raise InvalidInput("Password cannot be empty.")
        if len(password) < 6:
            raise InvalidInput("Password must contain at least 6 characters.")
        self.__password = password
    
    #---------------------- NORMAL METHODS ---------------------------

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if not self.check_password(old_password):
            raise InvalidInput("Old Password is Incorrect!")
        new_password = new_password.strip()
        if not new_password:
            raise InvalidInput("New Password cannot be empty.")
        if len(new_password) < 6:
            raise InvalidInput("New Password must contain at least 6 characters.")
        if old_password == new_password:
            raise InvalidInput("New Password must be different from the old password.")
        self.__password = new_password
        print("Password Changed Successfully!")
    
    def verify_login(self, person_id, password):
        return (self.person_id == person_id and self.check_password(password))

    def login(self):
        print(f"{self.name} logged In Successfully!")
    
    def logout(self):
        print(f"{self.name} logged Out Successfully!")
    
    def display(self):
        print("============== DETAILS ==============")
        print(f"ID               : {self.person_id}")
        print(f"NAME             : {self.name}")
        print(f"AGE              : {self.age}")
        print(f"GENDER           : {self.gender}")
        print(f"MOBILE           : {self.mobile}")
    
    #---------------------- STATIC METHOD ---------------------------
    
    @staticmethod
    def validate_mobile(mobile):
        mobile_str = str(mobile)
        if len(mobile_str) == 10:
            if not mobile_str.isdigit():
                return False
            if mobile_str.startswith(("6", "7", "8", "9")):
                return True
        return False
    
    @property
    def password(self):
        return self.__password

#======================================== STUDENT ========================================

class Student(Person):
    
    total_students = 0
    
    #---------------------- CONSTRUCTOR ---------------------------
    
    def __init__(self, person_id, name, age, gender, mobile, password,
                course, semester):
        
        super().__init__(person_id, name, age, gender, mobile, password)
        
        course = course.strip().upper()
        if course not in VALID_COURSES:
            raise InvalidInput(
                f"Course must be one of {', '.join(VALID_COURSES)}."
            )
        self.course = course

        if not (MIN_SEMESTER <= semester <= MAX_SEMESTER):
            raise InvalidInput(
                f"Semester must be between {MIN_SEMESTER} and {MAX_SEMESTER}."
            )
        self.semester = semester
        
        self.__subject_marks = {}
        
        self.attendance = {"present" : 0, "total_classes" : 0}
        
        self.fee = {"amount" : 50000, "paid" : False}
        
        Student.total_students += 1
    
    #---------------------- NORMAL METHODS ---------------------------
    
    def display(self):
        super().display()
        print(f"COURSE           : {self.course}")
        print(f"SEMESTER         : {self.semester}")
        print(f"FEE STATUS       : {'PAID' if self.fee['paid'] else 'PENDING'}")

    def calculate_percentage(self):
        if not self.subject_marks:
            return 0
        percentage = round(sum(self.subject_marks.values()) / len(self.subject_marks), 2)
        return percentage 
    
    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"
    
    def calculate_attendance(self):
        
        present = self.attendance["present"]
        total = self.attendance["total_classes"]
        
        if present > total:
            raise InvalidAttendanceError("Present classes cannot exceed total classes.")
        
        if present < 0 or total < 0:
            raise InvalidAttendanceError("Attendance cannot be negative.")
        
        if total == 0:
            raise InvalidAttendanceError("There were no classes till now.")
        
        absent = total - present
        percentage = round((present / total) * 100, 2)
        
        return present, absent, total, percentage
    
    def view_result(self):
        if not self.subject_marks:
            print("No Marks Assigned Yet!")
            return
        
        total_marks = sum(self.subject_marks.values())
        maximum_marks = len(self.subject_marks) * 100
        percentage = self.calculate_percentage()
        grade = self.calculate_grade()
        
        if grade == "F":
            result = "FAIL"
        else:
            result = "PASS"
        
        table = PrettyTable()
        table.align = "l"
        table.field_names = ["Subject", "Marks"]
        for subject, marks in self.subject_marks.items():
            table.add_row([subject, marks])
        
        print("\n" + "=" * 50)
        print("RESULT".center(50))
        print("=" * 50)
        
        print(table)
        
        print("-"*50)
        
        print(f"Total Marks      : {total_marks} / {maximum_marks}")
        print(f"Percentage       : {percentage} %")
        print(f"Grade            : {grade}")
        print(f"Result           : {result}")
    
    def pay_fee(self):
        if self.fee["paid"]:
            print("\nFee has already been paid.")
        else:
            self.fee["paid"] = True
            print(f'\n₹{self.fee["amount"]} fee paid successfully!')
    
    #---------------------- PROPERTY METHODS ---------------------------
    
    @property
    def subject_marks(self):
        return self.__subject_marks
    
    @subject_marks.setter
    def subject_marks(self, value):
        if not isinstance(value, dict):
            raise InvalidSubjectMarksError("Subject marks must be a dictionary.")
        if not value:
            raise InvalidSubjectMarksError("At least one subject is required.")
        for subject, marks in value.items():
            if not subject.strip():
                raise InvalidSubjectMarksError("Subject name cannot be empty.")
            if not isinstance(marks, (int, float)):
                raise InvalidSubjectMarksError(f"{subject} marks must be numeric.")
            if not (MIN_MARKS <= marks <= MAX_MARKS):
                raise InvalidSubjectMarksError(f"{subject} marks must be between {MIN_MARKS} and {MAX_MARKS}.")
        self.__subject_marks = value

    #---------------------- CLASS METHODS ---------------------------

    @classmethod
    def from_string(cls, student_string):
        data = student_string.split(",")
        return cls(
            data[0],
            data[1],
            int(data[2]),
            data[3],
            data[4],
            data[5],
            int(data[6])
        )
    
    #---------------------- MAGIC METHODS ---------------------------
    
    def __str__(self):
        return (
            f"Student(ID={self.person_id}, "
            f"Name={self.name}, "
            f"Course={self.course}, "
            f"Semester={self.semester})"
        )
        
    def __len__(self):
        return len(self.subject_marks)

#======================================== TEACHER ========================================

class Teacher(Person):
    
    total_teachers = 0
    
    #---------------------- CONSTRUCTOR ---------------------------
    
    def __init__(self, person_id, name, age, gender, mobile, password,
                subject, salary):
        
        super().__init__(person_id, name, age, gender, mobile, password)
        
        self.subject = subject
        self.salary = salary
        
        Teacher.total_teachers += 1
    
    #---------------------- NORMAL METHODS ---------------------------
    
    def display(self):
        super().display()
        print(f"SUBJECT          : {self.subject}")
        print(f"SALARY           : {self.salary}")
    
    def add_marks(self, student):
        print(f"\nAdding marks for {student.name}")
        
        subject = input("Enter Subject : ").strip().title()
        
        if len(subject) < 2:
            raise InvalidInput("Subject name must contain at least 2 characters.")
        
        if not all(ch.isalpha() or ch.isspace() for ch in subject):
            raise InvalidInput("Subject name can contain only alphabets and spaces.")
        
        try:
            marks = int(input("Enter Marks   : "))
        except ValueError:
            raise InvalidInput("Marks must be a number.")
        
        if not (MIN_MARKS <= marks <= MAX_MARKS):
            raise InvalidSubjectMarksError(f"Marks must be between {MIN_MARKS} and {MAX_MARKS}.")
        
        if subject in student.subject_marks:
            raise InvalidInput(f"{subject} marks already exist. Use Update Marks instead.")
        
        student.subject_marks[subject] = marks
        
        print(f"\n{subject} marks added successfully for {student.name}.")
    
    def update_marks(self, student):
        print(f"\nUpdating marks for {student.name}")
        
        subject = input("Enter Subject : ").strip().title()
        
        if len(subject) < 2:
            raise InvalidInput("Subject name must contain at least 2 characters.")

        if not all(ch.isalpha() or ch.isspace() for ch in subject):
            raise InvalidInput("Subject name can contain only alphabets and spaces.")
        
        if subject not in student.subject_marks:
            raise InvalidSubjectMarksError(f"{subject} marks not found.")
        
        try:
            marks = int(input("Enter Marks   : "))
        except ValueError:
            raise InvalidInput("Marks must be a number.")
        
        if not (MIN_MARKS <= marks <= MAX_MARKS):
            raise InvalidSubjectMarksError(f"Marks must be between {MIN_MARKS} and {MAX_MARKS}.")
        
        student.subject_marks[subject] = marks
        
        print(f"\n{subject} marks updated successfully for {student.name}.")
    
    def take_attendance(self, student):
        print(f"\nAttendance for {student.name}")
        choice = input("Present (Y/N): ").strip().upper()
        if choice not in ("Y", "N"):
            raise InvalidInput("Enter Y or N only.")
        student.attendance["total_classes"] += 1
        if choice == "Y":
            student.attendance["present"] += 1
            
    #---------------------- PROPERTY METHODS ---------------------------

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise InvalidInput("Salary must be numeric.")
        if value <= 0:
            raise InvalidInput("Salary must be greater than 0.")
        self.__salary = value

#======================================== ADMIN ========================================

class Admin(Person):
    
    total_admin = 0

    #---------------------- CONSTRUCTOR ---------------------------
    
    def __init__(self, person_id, name, age, gender, mobile, password):
        
        super().__init__(person_id, name, age, gender, mobile, password)
        
        Admin.total_admin += 1
    
    #---------------------- NORMAL METHODS ---------------------------
    
    def view_students(self, students):
        if not students:
            print("\nNo Students Found!")
            return
        table = PrettyTable()
        table.align = "l"
        table.field_names = [
            "ID",
            "Name",
            "Course",
            "Semester",
            "Attendance",
            "Fee Status"
        ]
        for student in students.values():
            fee_status = "Paid" if student.fee["paid"] else "Pending"
            table.add_row([
                student.person_id,
                student.name,
                student.course,
                student.semester,
                f"{student.calculate_attendance()[3]}%"
                if student.attendance["total_classes"] > 0 else "N/A",
                fee_status
            ])
        print("\n" + "=" * 80)
        print("STUDENT LIST".center(80))
        print("=" * 80)
        print(table)

    def view_teachers(self, teachers):
        if not teachers:
            print("\nNo Teachers Found!")
            return
        table = PrettyTable()
        table.align = "l"
        table.field_names = [
            "ID",
            "Name",
            "Subject",
            "Salary"
        ]
        for teacher in teachers.values():
            table.add_row([
                teacher.person_id,
                teacher.name,
                teacher.subject,
                teacher.salary
            ])
        print("\n" + "=" * 80)
        print("TEACHER LIST".center(80))
        print("=" * 80)
        print(table)

    def search_student(self, students):
        if not students:
            print("\nNo Students Found!")
            return
        keyword = input("Enter Student ID or Name : ").strip()
        if not keyword:
            raise InvalidInput("Search cannot be empty.")
        for student in students.values():
            if (
                student.person_id.upper() == keyword.upper()
                or student.name.lower() == keyword.lower()
            ):
                print("\nStudent Found!\n")
                student.display()
                return
        print("\nStudent Not Found!")

    def add_student(self, students):
        print("\nEnter Student Details\n")

        name = input("Name       : ").strip()
        if len(name) < 3:
            raise InvalidInput("Name must contain at least 3 characters.")
        if not all(ch.isalpha() or ch.isspace() for ch in name):
            raise InvalidInput("Name can contain only alphabets and spaces.")
        name = name.title()

        try:
            age = int(input("Age        : "))
        except ValueError:
            print("Age must be numeric.")
            return

        gender = input("Gender     : ").strip().title()

        mobile = input("Mobile     : ").strip()

        password = input("Password   : ").strip()

        course = input("Course     : ").strip().upper()

        try:
            semester = int(input("Semester   : "))
        except ValueError:
            print("Semester must be numeric.")
            return

        # Generate Student ID
        if students:
            last_id = max(int(student_id[1:]) for student_id in students.keys())
            student_id = f"S{last_id + 1}"
        else:
            student_id = "S501"

        try:
            student = Student(student_id, name, age, gender, mobile,
                password, course, semester)

            students[student.person_id] = student

            print("\nStudent Added Successfully!")
            print(f"Student ID : {student.person_id}")

        except (InvalidAgeError, InvalidMobileError, InvalidInput) as e:
            print(e)

    def add_teacher(self, teachers):
        print("\nEnter Teacher Details\n")

        name = input("Name       : ").strip()
        if len(name) < 3:
            raise InvalidInput("Name must contain at least 3 characters.")
        if not all(ch.isalpha() or ch.isspace() for ch in name):
            raise InvalidInput("Name can contain only alphabets and spaces.")
        name = name.title()

        try:
            age = int(input("Age        : "))
        except ValueError:
            print("Age must be numeric.")
            return

        gender = input("Gender     : ").strip().title()

        mobile = input("Mobile     : ").strip()

        password = input("Password   : ").strip()

        subject = input("Subject    : ").strip().title()

        try:
            salary = int(input("Salary     : "))
        except ValueError:
            print("Salary must be numeric.")
            return

        # Generate Teacher ID
        if teachers:
            last_id = max(int(teacher_id[1:]) for teacher_id in teachers.keys())
            teacher_id = f"T{last_id + 1}"
        else:
            teacher_id = "T51"

        try:
            teacher = Teacher( teacher_id, name, age, gender, mobile, password, subject, salary)
            teachers[teacher.person_id] = teacher
            print("\nTeacher Added Successfully!")
            print(f"Teacher ID : {teacher.person_id}")
        except ( InvalidAgeError, InvalidMobileError, InvalidInput) as e:
            print(e)

    def update_student(self, students):
        if not students:
            print("\nNo Students Found!")
            return

        student_id = input("Enter Student ID : ").strip().upper()
        if student_id not in students:
            print("\nStudent Not Found!")
            return
        student = students[student_id]

        print("\nLeave blank if you don't want to change a field.\n")

        # ---------------- Name ----------------

        name = input(f"Name [{student.name}] : ").strip()
        if name:
            if len(name) < 3:
                raise InvalidInput("Name must contain at least 3 characters.")
            if not all(ch.isalpha() or ch.isspace() for ch in name):
                raise InvalidInput("Name can contain only alphabets and spaces.")
            student.name = name.title()

        # ---------------- Age ----------------

        age = input(f"Age [{student.age}] : ").strip()
        if age:
            try:
                age = int(age)
            except ValueError:
                raise InvalidInput("Age must be numeric.")
            if not (MIN_AGE <= age <= MAX_AGE):
                raise InvalidAgeError(f"Age must be between {MIN_AGE} and {MAX_AGE}.")
            student.age = age

        # ---------------- Gender ----------------

        gender = input(f"Gender [{student.gender}] : ").strip().title()
        if gender:
            if gender not in VALID_GENDERS:
                raise InvalidInput(f"Gender must be one of {', '.join(VALID_GENDERS)}.")
            student.gender = gender

        # ---------------- Mobile ----------------

        mobile = input(f"Mobile [{student.mobile}] : ").strip()
        if mobile:
            if not Person.validate_mobile(mobile):
                raise InvalidMobileError("Invalid Mobile Number.")
            student.mobile = mobile

        # ---------------- Course ----------------

        course = input(f"Course [{student.course}] : ").strip().upper()
        if course:
            if course not in VALID_COURSES:
                raise InvalidInput(f"Course must be one of {', '.join(VALID_COURSES)}.")
            student.course = course

        # ---------------- Semester ----------------

        semester = input(f"Semester [{student.semester}] : ").strip()
        if semester:
            try:
                semester = int(semester)
            except ValueError:
                raise InvalidInput("Semester must be numeric.")
            if not (MIN_SEMESTER <= semester <= MAX_SEMESTER):
                raise InvalidInput(f"Semester must be between {MIN_SEMESTER} and {MAX_SEMESTER}.")
            student.semester = semester

        print("\nStudent details updated successfully!")

    def update_teacher(self, teachers):
        if not teachers:
            print("\nNo Teachers Found!")
            return

        teacher_id = input("Enter Teacher ID : ").strip().upper()
        if teacher_id not in teachers:
            print("\nTeacher Not Found!")
            return
        teacher = teachers[teacher_id]
        print("\nLeave blank if you don't want to change a field.\n")

        # ---------------- Name ----------------

        name = input(f"Name [{teacher.name}] : ").strip()
        if name:
            if len(name) < 3:
                raise InvalidInput("Name must contain at least 3 characters.")
            if not all(ch.isalpha() or ch.isspace() for ch in name):
                raise InvalidInput("Name can contain only alphabets and spaces.")
            teacher.name = name.title()

        # ---------------- Age ----------------

        age = input(f"Age [{teacher.age}] : ").strip()
        if age:
            try:
                age = int(age)
            except ValueError:
                raise InvalidInput("Age must be numeric.")
            if not (MIN_AGE <= age <= MAX_AGE):
                raise InvalidAgeError(f"Age must be between {MIN_AGE} and {MAX_AGE}.")
            teacher.age = age

        # ---------------- Gender ----------------

        gender = input(f"Gender [{teacher.gender}] : ").strip().title()
        if gender:
            if gender not in VALID_GENDERS:
                raise InvalidInput(f"Gender must be one of {', '.join(VALID_GENDERS)}.")
            teacher.gender = gender

        # ---------------- Mobile ----------------

        mobile = input(f"Mobile [{teacher.mobile}] : ").strip()
        if mobile:
            if not Person.validate_mobile(mobile):
                raise InvalidMobileError("Invalid Mobile Number.")
            teacher.mobile = mobile

        # ---------------- Subject ----------------

        subject = input(f"Subject [{teacher.subject}] : ").strip().title()
        if subject:
            if len(subject) < 2:
                raise InvalidInput("Subject name must contain at least 2 characters.")
            if not all(ch.isalpha() or ch.isspace() for ch in subject):
                raise InvalidInput("Subject name can contain only alphabets and spaces.")
            teacher.subject = subject

        # ---------------- Salary ----------------

        salary = input(f"Salary [{teacher.salary}] : ").strip()
        if salary:
            try:
                salary = int(salary)
            except ValueError:
                raise InvalidInput("Salary must be numeric.")
            teacher.salary = salary

        print("\nTeacher details updated successfully!")

    def delete_student(self, students):
        if not students:
            print("\nNo Students Found!")
            return
        student_id = input("Enter Student ID : ").strip().upper()
        if student_id not in students:
            print("\nStudent Not Found!")
            return
        confirm = input(f"Are you sure you want to delete {student_id}? (Y/N): ").strip().upper()
        if confirm == "Y":
            del students[student_id]
            Student.total_students -= 1
            print("\nStudent deleted successfully!")
        elif confirm == "N":
            print("\nDeletion cancelled.")
        else:
            print("\nInvalid Choice!")

    def delete_teacher(self, teachers):
        if not teachers:
            print("\nNo Teachers Found!")
            return
        teacher_id = input("Enter Teacher ID : ").strip().upper()
        if teacher_id not in teachers:
            print("\nTeacher Not Found!")
            return
        confirm = input(f"Are you sure you want to delete {teacher_id}? (Y/N): ").strip().upper()
        if confirm == "Y":
            del teachers[teacher_id]
            Teacher.total_teachers -= 1
            print("\nTeacher deleted successfully!")
        elif confirm == "N":
            print("\nDeletion cancelled.")
        else:
            print("\nInvalid Choice!")

#======================================== PRINCIPAL ========================================

class Principal(Person):

    #---------------------- CONSTRUCTOR ---------------------------
    
    def __init__(self, person_id, name, age, gender, mobile, password):
        super().__init__(person_id, name, age, gender, mobile, password)
    
    #---------------------- NORMAL METHODS ---------------------------
    
    def highest_percentage(self, students):
        if not students:
            print("\nNo Students Found!")
            return
        top_student = max(students.values(), key=lambda student: student.calculate_percentage())
        
        print("\n" + "=" * 50)
        print("HIGHEST PERCENTAGE".center(50))
        print("=" * 50)
        print(f"ID         : {top_student.person_id}")
        print(f"Name       : {top_student.name}")
        print(f"Percentage : {top_student.calculate_percentage()}%")
        
    def average_percentage(self, students):
        if not students:
            print("\nNo Students Found!")
            return
        average = sum(student.calculate_percentage() for student in students.values()) / len(students)
        print("\n" + "=" * 50)
        print("AVERAGE PERCENTAGE".center(50))
        print("=" * 50)
        print(f"Average Percentage : {round(average,2)}%")
    
    def top_three_students(self, students):
        if not students:
            print("\nNo Students Found!")
            return

        top_students = sorted(
            students.values(),
            key=lambda student: student.calculate_percentage(),
            reverse=True
        )[:3]
        table = PrettyTable()
        table.align = "l"
        table.field_names = ["Rank", "ID", "Name", "Percentage", "Grade"]
        for rank, student in enumerate(top_students, start=1):
            table.add_row([
                rank,
                student.person_id,
                student.name,
                f"{student.calculate_percentage()}%",
                student.calculate_grade()
            ])
        print("\n" + "=" * 70)
        print("TOP 3 STUDENTS".center(70))
        print("=" * 70)
        print(table)
    
    def pass_fail_report(self, students):
        if not students:
            print("\nNo Students Found!")
            return
        passed = 0
        failed = 0
        for student in students.values():
            if student.calculate_grade() == "F":
                failed += 1
            else:
                passed += 1
        print("\n" + "=" * 50)
        print("PASS / FAIL REPORT".center(50))
        print("=" * 50)
        print(f"Passed Students : {passed}")
        print(f"Failed Students : {failed}")
    
    def highest_attendance(self, students):
        if not students:
            print("\nNo Students Found!")
            return
        top_student = max(
            students.values(),
            key=lambda student: student.calculate_attendance()[3]
        )
        percentage = top_student.calculate_attendance()[3]

        print("\n" + "=" * 50)
        print("HIGHEST ATTENDANCE".center(50))
        print("=" * 50)

        print(f"ID         : {top_student.person_id}")
        print(f"Name       : {top_student.name}")
        print(f"Attendance : {percentage}%")
    
    def average_attendance(self, students):
        if not students:
            print("\nNo Students Found!")
            return

        average = sum(student.calculate_attendance()[3] for student in students.values()) / len(students)
        print("\n" + "=" * 50)
        print("AVERAGE ATTENDANCE".center(50))
        print("=" * 50)
        print(f"Average Attendance : {round(average,2)}%")
    
    def pending_fee_students(self, students):
        table = PrettyTable()
        table.align = "l"
        table.field_names = ["ID", "Name", "Amount"]
        found = False
        for student in students.values():
            if not student.fee["paid"]:
                found = True
                table.add_row([
                    student.person_id,
                    student.name,
                    student.fee["amount"]
                ])
        if not found:
            print("\nNo Pending Fees.")
            return
        print("\n" + "=" * 60)
        print("PENDING FEE STUDENTS".center(60))
        print("=" * 60)
        print(table)
    
    def college_summary(self, students, teachers, admins):
        if not students:
            print("\nNo Students Found!")
            return
        total_fee = sum(student.fee["amount"] for student in students.values())
        collected_fee = sum(
            student.fee["amount"]
            for student in students.values()
            if student.fee["paid"]
        )
        pending_fee = total_fee - collected_fee
        average_percentage = round(sum(student.calculate_percentage() for student in students.values()) / len(students),2)
        print("\n" + "=" * 60)
        print("COLLEGE SUMMARY".center(60))
        print("=" * 60)
        print(f"College Name        : Bridgefix College Management System")
        print(f"Total Students      : {len(students)}")
        print(f"Total Teachers      : {len(teachers)}")
        print(f"Total Admins        : {len(admins)}")
        print(f"Principal           : 1")
        print("-" * 60)
        print(f"Average Percentage  : {average_percentage}%")
        print(f"Fee Collected       : ₹{collected_fee}")
        print(f"Fee Pending         : ₹{pending_fee}")
        print("=" * 60)