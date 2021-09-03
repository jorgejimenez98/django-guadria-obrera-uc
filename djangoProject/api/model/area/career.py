from django.db import models
from .faculty import Faculty


class Career(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name='careers')
    name = models.CharField(max_length=69, unique=True)

    def __str__(self):
        return '{} | {}'.format(self.faculty.name, self.name)

    class Meta:
        unique_together = (('name', 'faculty'),)
        index_together = (('name', 'faculty'),)
