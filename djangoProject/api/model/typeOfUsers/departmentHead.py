from django.contrib.auth.models import User
from django.db import models
from ..area.department import Department


class DepartmentHead(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    department = models.OneToOneField(Department, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user.username} | {self.department.name}'

    class Meta:
        unique_together = (('user', 'department'),)
        index_together = (('user', 'department'),)
