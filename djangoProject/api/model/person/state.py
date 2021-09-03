from django.db import models


class State(models.Model):
    name = models.CharField(max_length=36, unique=True)
    typeOfPerson = models.CharField(max_length=56, default="", blank=True)

    def __str__(self):
        return '{} | {}'.format(self.name, self.typeOfPerson)
