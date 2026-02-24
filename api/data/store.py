"""Capa de almacenamiento en memoria para estudiantes."""

from copy import deepcopy

INITIAL_STUDENTS = [
    {"id": 1, "nombre": "Juan Pérez", "edad": 20, "carrera": "Ingeniería"},
    {"id": 2, "nombre": "María García", "edad": 22, "carrera": "Medicina"},
    {"id": 3, "nombre": "Carlos López", "edad": 21, "carrera": "Derecho"},
]


class StudentStore:
    def __init__(self):
        self.reset()

    def reset(self):
        self._students = deepcopy(INITIAL_STUDENTS)
        self._next_id = len(self._students) + 1

    def all(self):
        return self._students

    def by_id(self, student_id):
        return next((item for item in self._students if item["id"] == student_id), None)

    def add(self, student_data):
        student = {"id": self._next_id, **student_data}
        self._students.append(student)
        self._next_id += 1
        return student

    def update(self, student, new_data):
        student.update(new_data)
        return student

    def delete(self, student):
        self._students.remove(student)


store = StudentStore()
