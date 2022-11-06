import firebase_admin as fa
from firebase_admin import firestore, credentials
from models import Student
from icsparser import ParseICS

cred = credentials.Certificate("usocial-b56fa-5d111102e51b.json")
app = fa.initialize_app(cred)

db = firestore.client()
studentsCol = db.collection(u"students")


def get_student(username):
    student = studentsCol.document(username).get()
    if student.exists:
        return Student.fromDict(student.to_dict())


def get_students():
    students = []

    for s in studentsCol.stream():
        student = s.to_dict()
        students.append(Student.fromDict(student))

    return students


def username_exists(username: str) -> bool:
    exists = True

    students = get_students()
    for s in students:
        if s.username == username:
            exists = False
            break

    return exists


def add_student(username: str, pwd: str, icsF: str, faculty: str):
    courses = ParseICS(icsF).parse()
    student = Student(username, pwd, courses, faculty)

    if username_exists(username):
        studentsCol.document(username).set(student.toDict())


if __name__ == "__main__":
    path = input("Pass the .ics file ")

    content = ""
    with open(path) as f:
        content = f.read()

    username = input("Username? ")
    pwd = input("Password )> ")
    faculty = input("Faculty code: ")

    add_student(username, pwd, content, faculty)
