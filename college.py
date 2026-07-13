#================================ IMPORTS ====================================

from person import Student

#================================ LIBRARY ====================================

class Library:

    def issue_book(self, student, book_name):
        print(f"\nBook '{book_name}' issued to {student.name}.")

    def return_book(self, student, book_name):
        print(f"\nBook '{book_name}' returned by {student.name}.")


#================================ ACCOUNTS ====================================

class Accounts:

    def collect_fee(self, student):
        if student.fee["paid"]:
            print(f"\n{student.name} has already paid the fee.")
        else:
            student.fee["paid"] = True
            print(f"\n₹{student.fee['amount']} fee collected successfully.")

    def pending_fee(self, students):
        print("\nPending Fee Students\n")

        found = False

        for student in students.values():
            if not student.fee["paid"]:
                found = True
                print(f"{student.person_id} - {student.name}")

        if not found:
            print("No Pending Fees.")


#================================ CLASSROOM ====================================

class Classroom:

    def __init__(self):
        self.rooms = {
            "BCA": "Room 101",
            "BTECH": "Room 102",
            "MBA": "Room 201",
            "MCA": "Room 202",
            "BSC": "Room 301",
            "MSC": "Room 302",
            "MTECH": "Room 401",
            "BBA": "Room 402"
        }

    def allot_room(self, student):
        room = self.rooms.get(student.course, "Not Assigned")

        print("\nClassroom Details")
        print(f"Student : {student.name}")
        print(f"Course  : {student.course}")
        print(f"Room    : {room}")

    def display_rooms(self):
        print("\nAvailable Classrooms\n")

        for course, room in self.rooms.items():
            print(f"{course:<10} : {room}")


#================================ COLLEGE ====================================

class College:

    def __init__(self, name):

        self.name = name

        # Composition
        self.library = Library()
        self.accounts = Accounts()
        self.classroom = Classroom()

    def display_details(self):
        print("=" * 60)
        print(self.name.center(60))
        print("=" * 60)

        print(f"Total Students : {Student.total_students}")