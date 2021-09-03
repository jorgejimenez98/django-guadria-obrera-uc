from django.db import models
from .area.area import Area
from .area.universitySeat import UniversitySeat
from .area.faculty import Faculty
from .person.worker import Worker
from datetime import datetime


class OfficialDistributionOGS(models.Model):
    dayOfMonth = models.PositiveIntegerField(default=0)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, blank=True, null=True)
    universitySeat = models.ForeignKey(UniversitySeat, on_delete=models.PROTECT, related_name='officialDistributions')
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name='faculty', blank=True, null=True)
    guardOfficer = models.OneToOneField(Worker, blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        unique_together = (('dayOfMonth', 'universitySeat', 'guardOfficer'),)
        index_together = (('dayOfMonth', 'universitySeat', 'guardOfficer'),)

    def __str__(self):
        return '{} | {} | {} | {} | {}'.format(self.dayOfMonth,
                                               self.universitySeat.name,
                                               self.faculty.name,
                                               self.area.name,
                                               self.guardOfficer.names)

    def isNotRegistered(self):
        return self.guardOfficer is None and self.faculty is None and self.area is None

    @property
    def hasFaculty(self):
        return self.faculty is not None

    @property
    def hasGuardOfficer(self):
        return self.guardOfficer is not None

    @property
    def hasArea(self):
        return self.area is not None


def getTodayDetails(universitySeatName):
    todayOfficialDistributions = OfficialDistributionOGS.objects.filter(dayOfMonth=datetime.today().day)
    for i in todayOfficialDistributions:
        if i.universitySeat.name == universitySeatName:
            if i.guardOfficer is not None and i.faculty is not None:
                return """{} {}, {}
                        """.format(i.guardOfficer.names, i.guardOfficer.surnames, i.faculty.name)
            return 'OGS No registrado'
    return 'Distribucion Oficial no registrada'
