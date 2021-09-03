from django.db import models
from .area import Area


class Department(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name='departments')
    name = models.CharField(max_length=86)

    def __str__(self):
        return '{} | {}'.format(self.area.name, self.name)

    class Meta:
        unique_together = (('name', 'area'),)
        index_together = (('name', 'area'),)
