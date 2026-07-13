
MIN_MARKS = 0
MAX_MARKS = 100

class Person:
    
    def __init__(self, person_id, name, age, gender, mobile):
        self.person_id = person_id
        self.name = name
        if age < 18:
            raise Exception("Age must be greater than 18.")
        self.age = age
        self.gender = gender
        if not Person.validate_mobile(mobile):
            raise Exception("Invalid Mobile Number.")
        self.mobile = mobile
    
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
    
    #--------------STATIC METHOD------------------
    
    @staticmethod
    def validate_mobile(mobile):
        if len(mobile) == 10 and mobile.isdigit():
            return True
        return False

class Student(Person):
    
    total_students = 0
    
    # ---------------- Constructor ---------------- #
    
    def __init__(self, person_id, name, age, gender, mobile,
                course, semester):
        
        super().__init__(person_id, name, age, gender, mobile)
        
        self.course = course
        self.semester = semester
        self.__subject_marks = {}
        self.attendance = {
            "present" : 0,
            "total_classes" : 0
        }
        self.fee = {
            "amount" : 50000,
            "paid" : False
        }
        
        Student.total_students += 1
    
    # ---------------- Normal Methods ---------------- #
    
    def display(self):
        super().display()
        print(f"COURSE           : {self.course}")
        print(f"SEMESTER         : {self.semester}")

    def calculate_percentage(self):
        pass
    
    def calculate_grade(self):
        pass
    
    def calculate_attendance(self):
        pass
    
    def view_result(self):
        pass
    
    def pay_fee(self):
        pass
    
    #--------------STATIC METHOD------------------
    
    
    
    #--------------PROPERTY------------------
    
    @property
    def subject_marks(self):
        return self.__subject_marks
    
    @subject_marks.setter
    def subject_marks(self, value):
        if not isinstance(value, dict):
            raise Exception("Subject marks must be a dictionary.")
        for subject, marks in value.items():
            if not (MIN_MARKS <= marks <= MAX_MARKS):
                raise Exception(f"{subject} marks must be between {MIN_MARKS} and {MAX_MARKS}")
        self.__subject_marks = value
    
    #--------------MAGIC METHODS------------------
    
    # def __str__(self):
    #     return super().__str__()
    
    # def __len__(self):
    #     pass
    
    # def __eq__(self, value):
    #     return super().__eq__(value)

class Teacher(Person):
    
    total_teachers = 0
    
    # ---------------- Constructor ---------------- #
    
    def __init__(self, person_id, name, age, gender, mobile,
                subject, salary):
        
        super().__init__(person_id, name, age, gender, mobile)
        
        self.subject = subject
        self.__salary = salary
        
        Teacher.total_teachers += 1
    
    # ---------------- Normal Methods ---------------- #
    
    def display(self):
        super().display()
        print(f"SUBJECT          : {self.subject}")
        print(f"SALARY           : {self.salary}")
    
    def add_marks(self):
        pass
    
    def update_marks(self):
        pass
    
    def take_attendance(self):
        pass
    
    #--------------PROPERTY METHOD------------------
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        pass

class Admin(Person):
    
    total_admin = 0
    
    def __init__(self, person_id, name, age, gender, mobile):
        
        super().__init__(person_id, name, age, gender, mobile)
        
        Admin.total_admin += 1
    
    def add_student(self):
        pass
    
    def delete_student(self):
        pass
    
    def search_student(self, *args):
        pass
    
    def add_teacher(self):
        pass
    
    def view_students(self):
        pass
    
    def view_teachers(self):
        pass

class Principal(Person):
    
    def __init__(self, person_id, name, age, gender, mobile):
        super().__init__(person_id, name, age, gender, mobile)
    
    def top_three_students(self):
        pass

    def highest_percentage(self):
        pass

    def average_percentage(self):
        pass

    def pass_fail_report(self):
        pass
