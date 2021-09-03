from django.db import models

from .guard import Guard
from ..person.worker import Worker


class WorkersGuard(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.PROTECT, related_name='workersGuards')
    assistance = models.BooleanField(default=False)
    departmentId = models.PositiveIntegerField(default=0)
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    isOGS = models.BooleanField(default=False)

    def __str__(self):
        return """{} | {} | {} | {}""".format(self.guard.date, self.worker.names + " " + self.worker.surnames,
                                              self.guard.universitySeat.name, self.isOGS)
