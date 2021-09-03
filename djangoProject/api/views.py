from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .model.area.universitySeat import UniversitySeat
from .model.guard.guard import Guard
from .helpFiles.guardFunctions import getGuardByUniversitySeatName
from .helpFiles.dateFunctions import *


def homeView(request):
    if not request.user.is_authenticated:
        guardList = Guard.objects.all().filter(date=getTodayDayOnAString())
        if guardList.all().count() == 0:
            return redirect('noGuardsView')
        context = {
            'guardList': guardList if guardList.all().count() != 0 else None,
            'joseMartiGuard': getGuardByUniversitySeatName('Jose Martí', guardList),
            'fajardoGuard': getGuardByUniversitySeatName('Fajardo', guardList),
            'agramonteGuard': getGuardByUniversitySeatName('Ignacio Agramonte Loynaz', guardList),
            'today': getTodayDayOnACompleteString()
        }
        return render(request, 'public/home.html', context)
    return redirect('administrationPanelView')


@login_required(login_url='/')
def administrationPanelView(request):
    context = {
        'today': getTodayDayOnACompleteString(),
        'universitySeats': UniversitySeat.objects.all(),
        'todayDay': date.day,
        'thereAreNotReports': not UniversitySeat.objects.get(
            pk=4).isOfficialDistributionOGSPublished and not UniversitySeat.objects.get(
            pk=3).isOfficialDistributionOGSPublished and not UniversitySeat.objects.get(
            pk=2).isOfficialDistributionOGSPublished
    }
    return render(request, 'panel/dashboard.html', context)


def noGuardsView(request):
    return render(request, 'public/noGuards.html', {'today': getTodayDayOnACompleteString()})


def error404NotFoundView(request):
    return render(request, 'error404.html')


def error403AccessDeniedError(request):
    return render(request, 'error403.html')
