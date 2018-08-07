class Garden(object):

    plants_dict = {
        'V': 'Violets',
        'R': 'Radishes',
        'G': 'Grass',
        'C': 'Clover',
    }

    def __init__(self, diagram, students=None):
        self.diagram = diagram

        if students:
            self.students = sorted(students)
        else:
            self.students = students


stu = ['Manoj', 'Golu', 'Pranshu', 'Amruta']
c1 = Garden('VVCC\nCCVV', stu)
c2 = Garden('VVVV\nCCCC', 'We are the students')


print("C1 Diagram = {!r}". format(c1.diagram))
print("C1 students = {}".format(c1.students))
print(stu)
