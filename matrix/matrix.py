class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def rows(self):
        return [[int(n) for n in i.split()] for i in self.matrix.split('\n')]

    @property
    def columns(self):
        return list(map(list, zip(*self.rows)))
