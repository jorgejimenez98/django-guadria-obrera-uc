from django.db import models
from .state import State


class Person(models.Model):
    CI = models.CharField(max_length=11, unique=True, primary_key=True)
    names = models.CharField(max_length=126)
    surnames = models.CharField(max_length=126)
    sex = models.CharField(max_length=1)
    lastStatusUpdateDate = models.DateTimeField(auto_now=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
