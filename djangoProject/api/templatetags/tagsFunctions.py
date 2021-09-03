from django import template
from ..model.area.career import Career, Faculty
from ..helpFiles.extra import getUserRolInAString
from ..model.officialDistributionOGS import OfficialDistributionOGS

register = template.Library()


@register.filter(name='isSeatGuard')
def isSeatGuard(guard, universityName):
    return guard.universitySeat.name == universityName


@register.filter(name='getAllOfficialDistributionBySeat')
def getAllOfficialDistributionBySeat(seat):
    return OfficialDistributionOGS.objects.filter(universitySeat_id=seat.pk)


@register.filter(name='has_group')
def has_group(user, group_name):
    if user.groups.filter(name='Superusuario').exists():
        return True
    return user.groups.filter(name=group_name).exists()


@register.filter(name='getCareersByFaculty')
def getCareersByFaculty(facultyId):
    return Career.objects.filter(faculty=Faculty.objects.get(pk=int(facultyId)))


@register.filter(name='getGroup')
def getGroup(user):
    return getUserRolInAString(user)


@register.filter(name='getSmallEmail')
def getSmallEmail(user):
    return user.email.split('@')[0]


@register.filter(name='isNormalUser')
def isNormalUser(user):
    group = getUserRolInAString(user)
    return group not in 'Decano;Jefe Departamento;PPAA;Programador Facultad'.split(';')
