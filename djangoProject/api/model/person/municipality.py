from django.db import models
from .province import Province


class Municipality(models.Model):
    province = models.ForeignKey(Province, on_delete=models.PROTECT, related_name='municipalities')
    name = models.CharField(max_length=36)

    def __str__(self):
        return '{}| {} | {}'.format(self.pk, self.province.name, self.name)

    class Meta:
        unique_together = (('name', 'province'),)
        index_together = (('name', 'province'),)
