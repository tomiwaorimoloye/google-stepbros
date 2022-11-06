import firebase_admin as fa
from firebase_admin import firestore, credentials
from models import Student
from icsparser import ParseICS


class FirebaseDB:
    def __init__(self):
        cred = credentials.Certificate("usocial-b56fa-5d111102e51b.json")
        fa.initialize_app(cred)

        db = firestore.client()
        self.__studentsCol = db.collection(u"students")

    def get_student(self, username):
        student = self.__studentsCol.document(username).get()
        if student.exists:
            return Student.fromDict(student.to_dict())

    def get_students(self) -> "list[Student]":
        students = []

        for s in self.__studentsCol.stream():
            student = s.to_dict()
            students.append(Student.fromDict(student))

        return students

    def username_exists(self, username: str) -> bool:
        exists = True

        students = self.get_students()
        for s in students:
            if s.username == username:
                exists = False
                break

        return exists

    def add_student(self, username: str, pwd: str, icsF: str, faculty: str):
        if self.username_exists(username):
            courses = ParseICS(icsF).parse()
            student = Student(username, pwd, courses, faculty)

            self.__studentsCol.document(username).set(student.toDict())


if __name__ == "__main__":
    path = input("Pass the .ics file ")

    content = ""
    with open(path) as f:
        content = f.read()

    username = input("Username? ")
    pwd = input("Password )> ")
    faculty = input("Faculty code: ")

    FirebaseDB().add_student(username, pwd, content, faculty)
