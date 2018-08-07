from collections import defaultdict


class School(object):
    """
    Allows to maintain a roster of students belonging to different grades in a school.
    """

    def __init__(self):
        """
        The constructor class. We define the default dict object here pertaining to each instance.
        """
        self.students_enrolled = defaultdict(list)

    def add_student(self, name, grade):
        """
        Method to add a student to a particular grade in the school roster.
        """
        self.students_enrolled[grade].append(name)

    def roster(self):
        """
        Returns a sorted list of students enrolled in the entire school.
        Sorting is done
        1. Grade wise
        2. Name wise
        """

        grades = sorted(self.students_enrolled.keys())
        return [student for grade in grades for student in self.grade(grade)]

    def grade(self, grade_number):
        return sorted(self.students_enrolled[grade_number])

    def __repr__(self):
        return "I am the schools roster database. Have you enrolled yet?"
