from collections import defaultdict

DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']


class Garden(object):
    """
    Allots the plants of each row to the students ordered alphabetically.
    """
    # We declare the class dictionary of common abbreviations here.
    abbreviations = {
        'V': 'Violets',
        'R': 'Radishes',
        'G': 'Grass',
        'C': 'Clover',
    }

    def __init__(self, diagram, students=None):

        self.students = sorted(students or DEFAULT_STUDENTS)

        # We use a defaultdict for each instance of the class.
        self.plants_of_each_student = defaultdict(list)

        # x --> row1, y --> row2
        x, y = diagram.split('\n')

        # We run the loop only till the length of the students list.
        for i in range(len(self.students)):
            j = i * 2  # To take 2 plants for each student
            self.plants_of_each_student[self.students[i]] = [self.abbreviations[x] for x in x[j:j + 2] + y[j:j + 2]]

    def plants(self, name):
        """
        Simply returns the list of plants pertaining to each student
        """
        return self.plants_of_each_student[name]
