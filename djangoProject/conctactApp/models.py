from django.db import models


# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=56, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=36, default='')
    typeOfPerson = models.CharField(max_length=36, default='')
    subject = models.CharField(max_length=124, default='')
    message = models.TextField(default='')

    def __str__(self):
        return f'{self.id} | {self.name} | {self.subject}'
