class Garden(object):
    PLANTS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    CUPS = [range(0, 24)[i:i + 2] for i in range(0, 24, 2)]

    def __init__(self, rows, students=None):
        self.rows = [list(i) for i in rows.split('\n')]
        self.students = self.student_names(students)

    def plants(self, student):
        plant_names = []
        loc = self.student_locations(student)
        for r in self.rows:
            plant_names.extend([r[loc[0]], r[loc[1]]])
        return [Garden.PLANTS[p] for p in plant_names]

    def student_locations(self, student):
        cup_locations = dict(zip(self.students, Garden.CUPS))
        return cup_locations[student]

    def student_names(self, students):
        if students is None:
            return ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                    'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            return sorted(students)
