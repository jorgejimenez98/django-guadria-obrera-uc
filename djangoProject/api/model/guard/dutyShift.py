from django.db import models


class DutyShift(models.Model):
    schedule = models.CharField(max_length=36, default='', unique=True)

    def __str__(self):
        return '{} | {}'.format(self.id, self.schedule)

