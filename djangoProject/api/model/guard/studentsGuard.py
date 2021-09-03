from django.db import models

from ..person.student import Student
from .guard import Guard
from .dutyShift import DutyShift


class StudentsGuard(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.PROTECT, related_name='studentsGuards')
    assistance = models.BooleanField(default=False)
    careerId = models.PositiveIntegerField(default=0, blank=True) # Se llena cuando se inserta una guardia
    yearOfStudy = models.PositiveIntegerField(default=0, blank=True) # Se llena cuando se inserta una guardia
    dutyShift = models.ForeignKey(DutyShift, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self):
        return """{} | {} | {}""".format(self.guard.date, self.student.names + ' ' + self.student.surnames, self.guard.universitySeat.name)
