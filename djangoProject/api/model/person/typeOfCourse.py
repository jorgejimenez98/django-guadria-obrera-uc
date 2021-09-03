from django.db import models


class TypeOfCourse(models.Model):
    name = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.name
