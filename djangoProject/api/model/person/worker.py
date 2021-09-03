from django.db import models
from .person import Person
from ..area.department import Department


class Worker(Person):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='workers')

    def __str__(self):
        return """{} | {} | {} | {}""".format(self.names, self.surnames, self.department.area.name, self.department.name)
