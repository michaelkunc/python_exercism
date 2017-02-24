from collections import defaultdict


class School(object):

    def __init__(self, name):
        self.name = name
        self.students = defaultdict(list)

    def grade(self, grade):
        return self.students[grade]

    def add(self, student, grade):
        self.students[grade].append(student)

    def sort(self):
        return ((grade, tuple(students)) for grade, students in self.students.items())
