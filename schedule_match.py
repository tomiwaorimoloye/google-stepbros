from icsparser import Student
from datetime import datetime


class TopNMatches:
    def get_n_matches(self,
                      student: Student,
                      otherStudents: "list[Student]",
                      n: int):

        possibleMatches = []

        studentCourses = student.courses
        for s in otherStudents:
            matchNo = 0

            for course in s.courses:
                for sCourse in studentCourses:
                    # Check times
                    if (course.sch.days & sCourse.sch.days):
                        if course.sch.startTime == sCourse.sch.startTime\
                                and course.sch.endTime == course.sch.endTime:
                            matchNo += 10

                    # Check classes
                    if course.title == sCourse.title:
                        matchNo += 2.5
                        if course.section == sCourse.section:
                            matchNo += 2.5

            possibleMatches.append((s, matchNo))

        sortedMatches = sorted(
            possibleMatches, key=lambda pair: pair[1], reverse=True)

        if len(sortedMatches) > n:
            sortedMatches = sortedMatches[:n]

        return [s for s, _ in sortedMatches]
