from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.decorators import checkUserAccess
from ....model.area.universitySeat import UniversitySeat
from ....model.officialDistributionAOGS import OfficialDistributionAOGS


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'joseMartiDetails': UniversitySeat.objects.get(pk=3),
        'agramonteDetails': UniversitySeat.objects.get(pk=2),
        'fajardoDetails': UniversitySeat.objects.get(pk=4),
    }
    return context


@login_required(login_url='/')
@checkUserAccess('Programador UC', login_url='/error403/')
def officialDistributionAOGS(request):
    for i in OfficialDistributionAOGS.objects.all():
        print(i)
    return render(request, 'panel/guardsStuff/officialDistributionAOGS/allSeats.html', getViewContext())
