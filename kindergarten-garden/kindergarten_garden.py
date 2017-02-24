class Garden(object):
    PLANTS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    CUPS = [range(0, 12)[i:i + 2] for i in range(0, 12, 2)]

    def __init__(self, rows):
        self.rows = [list(i) for i in rows.split('\n')]

    def plants(self, student):
        plant_names = []
        loc = self.student_locations()
        loc = loc[student]
        for r in self.rows:
            plant_names.extend([r[loc[0]], r[loc[1]]])
        return [Garden.PLANTS[p] for p in plant_names]

    def student_locations(self):
        return dict(zip(Garden.STUDENTS, Garden.CUPS))
