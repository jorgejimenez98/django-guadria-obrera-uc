from django.contrib.auth.models import User
from django.db import models
from ..area.career import Career


class PPAA(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    career = models.ForeignKey(Career, on_delete=models.PROTECT)
    yearOfStudy = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.user.username} | {self.career.name} | {self.yearOfStudy}'

    class Meta:
        unique_together = (('career', 'yearOfStudy'),)
        index_together = (('career', 'yearOfStudy'),)
