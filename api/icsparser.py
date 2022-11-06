from datetime import datetime
from models import Course, CourseSchedule


class ParseICS:
    def __init__(self, icsFile: str) -> None:
        assert icsFile is not None

        self.__file = icsFile.splitlines()

        assert len(self.__file) > 23
        self.__file = self.__file[23:]

    # Format -> Canada/Mountain:20220902T140000
    def __str_to_date(self, s: str):
        t = s.split(":")[1].split("T")[1]
        return datetime.strptime(t, "%H%M%S")

    def parse(self) -> "list[Course]":
        courses = []

        dtStart = None
        summary = ""
        dtEnd = None
        location = ""
        days = set()

        for line in self.__file:
            line = line.strip()

            if line == "BEGIN:VEVENT":
                dtStart = None
                summary = ""
                dtEnd = None
                location = ""
                days = set()
            elif "DTSTART" in line:
                starting = line.index("=") + 1
                dtStart = self.__str_to_date(line[starting:])
            elif "SUMMARY" in line:
                starting = line.index(":") + 1
                summary = line[starting:]
            elif "DTEND" in line:
                starting = line.index("=") + 1
                dtEnd = self.__str_to_date(line[starting:])
            elif "LOCATION" in line:
                starting = line.index(":") + 1
                location = line[starting:]
            elif "BYDAY" in line:
                starting = line.index("BYDAY=") + len("BYDAY=")
                days = set(line[starting:].split(";")[0].split(","))
            elif line == "END:VEVENT":
                summary = summary.split()
                sch = CourseSchedule(dtStart, dtEnd, days)

                courses.append(
                    Course(" ".join(summary[0:2]),
                           " ".join(summary[2:]),
                           location,
                           sch))

        return courses


if __name__ == "__main__":
    path = input("Where the .ics file? ")

    with open(path) as f:
        parser = ParseICS(f.read())
        print(*parser.parse(), sep="\n\n")
