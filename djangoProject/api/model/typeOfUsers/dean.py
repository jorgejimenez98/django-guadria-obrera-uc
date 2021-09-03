from django.contrib.auth.models import User
from django.db import models
from ..area.faculty import Faculty


class Dean(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    faculty = models.OneToOneField(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user.username} | {self.faculty.name}'

    class Meta:
        unique_together = (('user', 'faculty'),)
        index_together = (('user', 'faculty'),)
