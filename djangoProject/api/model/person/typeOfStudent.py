from django.db import models


class TypeOfStudent(models.Model):
    name = models.CharField(max_length=37, unique=True)

    def __str__(self):
        return self.name
