from django.db import models
from ..area.universitySeat import UniversitySeat


class Guard(models.Model):
    date = models.DateField(auto_now=False)
    incidents = models.TextField(default='')
    observations = models.TextField(default='')
    universitySeat = models.ForeignKey(UniversitySeat, on_delete=models.PROTECT, related_name='guards')

    class Meta:
        unique_together = (('date', 'universitySeat'),)
        index_together = (('date', 'universitySeat'),)

    def __str__(self):
        return """{} || {} || {}""".format(self.pk, self.date, self.universitySeat.name)

