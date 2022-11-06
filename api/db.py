import firebase_admin as fa
from firebase_admin import firestore, credentials
from models import Student, Course

cred = credentials.Certificate("usocial-b56fa-5d111102e51b.json")
app = fa.initialize_app(cred)

db = firestore.client()
studentsCol = db.collection(u"students")


def get_students():
    students = []

    for s in studentsCol.stream():
        student = s.to_dict()

        students.append(Student(
            student.get("username"),
            student.get("password"),
            [Course.fromDict(c) for c in student.get("courses")],
            student.get("faculty")
        ))

    return students


def username_exists(username: str) -> bool:
    exists = True

    students = studentsCol.stream()
    for s in students:
        if s.to_dict()["username"] == username:
            exists = False
            break

    return exists


def add_student(student: Student):
    if username_exists(student.username):
        studentsCol.add(student.toDict())
