from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=56, unique=True)
    abbreviation = models.CharField(max_length=12)

    def __str__(self):
        return '{} | {}'.format(self.id, self.name)



