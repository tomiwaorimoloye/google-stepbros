from datetime import datetime


class CourseSchedule:
    def __init__(self, startTime: str, endTime: str, days: set):
        self.startTime = self.str_to_date(startTime)
        self.endTime = self.str_to_date(endTime)
        self.days = days

    # Format -> Canada/Mountain:20220902T140000
    def str_to_date(self, s: str):
        t = s.split(":")[1].split("T")[1]
        return datetime.strptime(t, "%H%M%S")

    def __str__(self) -> str:
        string = ", ".join(self.days)
        string += f" {self.startTime.hour}:{self.startTime.minute:0>2}"
        string += f" to {self.endTime.hour}:{self.endTime.minute}"

        return string


class Course:
    def __init__(self,
                 summary: str,
                 location: str,
                 startTime: str, endTime: str,
                 days: set):
        summary = summary.split()

        self.title = " ".join(summary[0:2])
        self.section = None
        self.location = location
        self.sch = CourseSchedule(startTime, endTime, days)

        if len(summary) > 2:
            self.section = " ".join(summary[2:])

    def __str__(self) -> str:
        string = "Course title: " + self.title
        string += "\nSection: " + self.section
        string += "\nLocation: " + self.location
        string += "\nSchedule: " + str(self.sch)

        return string


class Student:
    faculties = {
        "AH": "Faculty of Agricultural, Life and Environmental Sciences",
        "AR": "Faculty of Arts",
        "AU": "Augustana Faculty",
        "BC": "Faculty of Business",
        "ED": "Faculty of Education",
        "EN": "Faculty of Engineering",
        "GS": "Faculty of Graduate Studies and Research",
        "LA": "Faculty of Law",
        "MH": "Faculty of Medicine and Dentistry",
        "NS": "Faculty of Native Studies",
        "NU": "Faculty of Nursing",
        "PE": "Faculty of Kinesiology, Sport, and Recreation",
        "PH": "Faculty of Pharmacy and Pharmaceutical Sciences",
        "PS": "School of Public Health",
        "RM": "Faculty of Rehabilitation Medicine",
        "SA": "Faculté Saint-Jean",
        "SC": "Faculty of Science",
        "SS": "St Stephen's College",
    }

    def __init__(self, username: str, courses: "list[Course]", faculty: str):
        assert len(courses) > 0 and isinstance(courses[0], Course)
        assert len(faculty) == 2, "Invalid faculty"

        self.username = username
        self.courses = courses
        self.faculty = Student.faculties.get(faculty, "Faculty of Unknown")
