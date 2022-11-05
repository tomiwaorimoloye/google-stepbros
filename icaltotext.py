# Created by Obaloluwa Odelana 5/Nov/2022

from os.path import isfile
from datetime import datetime


class CourseSchedule:
    def __init__(self, startTime: str, endTime: str, days: str):
        self.startTime = self.str_to_date(startTime)
        self.endTime = self.str_to_date(endTime)

        # Format -> MO,WE,FR;WKST=SU
        self.days = days.split(";")[0].split(",")

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
    def __init__(self, summary: str, location, startTime, endTime, sch):
        summary = summary.split()

        self.title = " ".join(summary[0:2])
        self.section = None
        self.location = location
        self.sch = CourseSchedule(startTime, endTime, sch)

        if len(summary) > 2:
            self.section = " ".join(summary[2:])

    def __str__(self) -> str:
        string = "Course title: " + self.title
        string += "\nSection: " + self.section
        string += "\nLocation: " + self.location
        string += "\nSchedule: " + str(self.sch)

        return string


class ParseICS:
    def __init__(self, path) -> None:
        assert isfile(path), f"'{path}' is not a file"
        assert ".ics" in path, "Wrong file format"

        try:
            file = open(path)
        except OSError:
            raise Exception(f"Cannot access file '{path}'")
        finally:
            file.close()

        self.path = path

    def parse(self) -> "list[Course]":
        courses = []

        with open(self.path) as f:
            for _ in range(23):
                next(f)

            dtStart = ""
            summary = ""
            dtEnd = ""
            location = ""
            days = ""

            for line in f:
                line = line.strip()

                if line == "BEGIN:VEVENT":
                    dtStart = ""
                    summary = ""
                    dtEnd = ""
                    location = ""
                    days = ""
                elif "DTSTART" in line:
                    starting = line.index("=") + 1
                    dtStart = line[starting:]
                elif "SUMMARY" in line:
                    starting = line.index(":") + 1
                    summary = line[starting:]
                elif "DTEND" in line:
                    starting = line.index("=") + 1
                    dtEnd = line[starting:]
                elif "LOCATION" in line:
                    starting = line.index(":") + 1
                    location = line[starting:]
                elif "BYDAY" in line:
                    starting = line.index("BYDAY=") + len("BYDAY=")
                    days = line[starting:]
                elif line == "END:VEVENT":
                    courses.append(
                        Course(summary, location, dtStart, dtEnd, days))

        return courses


if __name__ == "__main__":
    path = input("Where the .ics file? ")

    parser = ParseICS(path)
    print(*parser.parse(), sep="\n\n")
