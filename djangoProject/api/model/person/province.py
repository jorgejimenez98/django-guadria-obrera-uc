from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return '{} | {}'.format(self.pk, self.name)
