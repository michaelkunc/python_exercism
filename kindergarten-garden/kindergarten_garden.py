class Garden(object):
    PLANTS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, rows):
        self.rows = rows.split('\n')
        self.plant_names = self.plant_names(list(rows.replace('\n', '')))

    def plants(self, student):
        columns = Garden.STUDENTS.index(
            student), Garden.STUDENTS.index(student) + 1
        return self.plant_names[columns[0]]

    def plant_names(self, rows):
        return [Garden.PLANTS[i] for i in rows]
