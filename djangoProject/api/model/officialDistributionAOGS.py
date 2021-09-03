from django.db import models
from .officialDistributionOGS import OfficialDistributionOGS
from .person.worker import Worker


class OfficialDistributionAOGS(models.Model):
    number = models.PositiveIntegerField(default=0)
    officialDistribution = models.ForeignKey(OfficialDistributionOGS, on_delete=models.PROTECT, related_name='AOGS_distributions', default=None)
    guardOfficerHelper = models.OneToOneField(Worker, on_delete=models.PROTECT, default=None)

    class Meta:
        unique_together = (('number', 'officialDistribution', 'guardOfficerHelper'),)
        index_together = (('number', 'officialDistribution', 'guardOfficerHelper'),)

    def __str__(self):
        return """
            Number: {}
            Official Distribution: {}
            Guard Officer Helper: {}
        """.format(self.number, self.officialDistribution, self.guardOfficerHelper)
