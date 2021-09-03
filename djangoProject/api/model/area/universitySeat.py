from django.db import models


class UniversitySeat(models.Model):
    name = models.CharField(max_length=36, unique=True)
    AOGS_Cuantity = models.PositiveIntegerField()
    isOfficialDistributionOGSPublished = models.BooleanField(default=False)
    
    def __str__(self):
        return '{} | {}'.format(self.name, self.id)
