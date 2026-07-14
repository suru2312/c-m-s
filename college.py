#================================ IMPORTS ====================================

from person import Student, Teacher, Admin


#================================ LIBRARY ====================================

class Library:

    def issue_book(self, student, book_name):
        print(f"\n'{book_name}' has been issued to {student.name}.")

    def return_book(self, student, book_name):
        print(f"\n'{book_name}' has been returned by {student.name}.")


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

    def view_classroom(self, student):
        room = self.rooms.get(student.course, "Not Assigned")

        print("\n" + "=" * 50)
        print("CLASSROOM DETAILS".center(50))
        print("=" * 50)
        print(f"Student : {student.name}")
        print(f"Course  : {student.course}")
        print(f"Room    : {room}")

    def display_rooms(self):
        print("\n" + "=" * 50)
        print("AVAILABLE CLASSROOMS".center(50))
        print("=" * 50)

        for course, room in self.rooms.items():
            print(f"{course:<10} : {room}")


#================================ COLLEGE ====================================

class College:

    def __init__(self, name):

        self.name = name

        # Composition
        self.library = Library()
        self.classroom = Classroom()