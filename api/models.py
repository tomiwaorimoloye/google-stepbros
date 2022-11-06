class CourseSchedule:
    def __init__(self, startTime, endTime, days: set):
        self.startTime = startTime
        self.endTime = endTime
        self.days = days

    def __str__(self) -> str:
        string = ", ".join(self.days)
        string += f" {self.startTime.hour}:{self.startTime.minute:0>2}"
        string += f" to {self.endTime.hour}:{self.endTime.minute}"

        return string

    @classmethod
    def fromDict(cls, d: dict):
        return cls(
            startTime=d["startTime"],
            endTime=d["endTime"],
            days=set(d["days"])
        )

    def toDict(self):
        return {
            "startTime": self.startTime,
            "endTime": self.endTime,
            "days": list(self.days)
        }


class Course:
    def __init__(self,
                 title: str,
                 section: str,
                 location: str,
                 sch: CourseSchedule):
        self.title = title
        self.section = section
        self.location = location
        self.sch = sch

    def __str__(self) -> str:
        string = "Course title: " + self.title
        string += "\nSection: " + self.section
        string += "\nLocation: " + self.location
        string += "\nSchedule: " + str(self.sch)

        return string

    @classmethod
    def fromDict(cls, d: dict):
        return cls(
            title=d["title"],
            section=d["section"],
            location=d["location"],
            sch=CourseSchedule.fromDict(d["schedule"])
        )

    def toDict(self):
        return {
            "title": self.title,
            "section": self.section,
            "location": self.location,
            "schedule": self.sch.toDict()
        }


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

    def __init__(self,
                 username: str, password: str,
                 courses: "list[Course]",
                 faculty: str):
        assert len(courses) > 0 and isinstance(courses[0], Course)

        self.username = username
        self.password = password
        self.courses = courses
        self.faculty = Student.faculties.get(faculty, "Faculty of Unknown")\
            if len(faculty) == 2 else faculty

    @classmethod
    def fromDict(cls, d: dict):
        return cls(
            username=d["username"],
            password=d["password"],
            courses=[Course.fromDict(c) for c in d["courses"]],
            faculty=d["faculty"]
        )

    def toDict(self):
        return {
            "username": self.username,
            "password": self.password,
            "courses": [c.toDict() for c in self.courses],
            "faculty": self.faculty
        }
