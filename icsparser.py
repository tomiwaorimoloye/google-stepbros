from os.path import isfile
from models import Course


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
            days = set()

            for line in f:
                line = line.strip()

                if line == "BEGIN:VEVENT":
                    dtStart = ""
                    summary = ""
                    dtEnd = ""
                    location = ""
                    days = set()
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
                    days = set(line[starting:].split(";")[0].split(","))
                elif line == "END:VEVENT":
                    courses.append(
                        Course(summary, location, dtStart, dtEnd, days))

        return courses


if __name__ == "__main__":
    path = input("Where the .ics file? ")

    parser = ParseICS(path)
    print(*parser.parse(), sep="\n\n")
