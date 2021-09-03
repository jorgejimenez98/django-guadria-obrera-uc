from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.decorators import checkUserAccess
from ....model.area.area import Area
from ....helpFiles.extra import *


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'areaList': Area.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def areasList(request):
    return render(request, 'panel/univesityStuff/area/areaList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addArea(request):
    context = getViewContext()
    context['area'] = None
    if request.method == 'POST':
        name = request.POST.get('name')
        abbreviation = request.POST.get('abv')
        try:
            validateString(name, 'Nombre Área Docente')
            validateString(abbreviation, 'Abreviación')
            Area.objects.create(name=name, abbreviation=abbreviation)
            messages.success(request, getAddedSuccessMessage('Área Docente', name))
            return redirect('areasList')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Área Docente', name))
            return render(request, 'panel/univesityStuff/area/addOrEditArea.html', context)
        except Exception as e:
            messages.error(request, e.args[0])
            return render(request, 'panel/univesityStuff/area/addOrEditArea.html', context)
    return render(request, 'panel/univesityStuff/area/addOrEditArea.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteArea(request, pk):
    area = Area.objects.get(pk=pk)
    try:
        area.delete()
        messages.success(request, getEliminateSuccessMessage('Área', area.name))
        return redirect('areasList')
    except ProtectedError:
        messages.error(request, getEliminateProtectErrorMessage('Área', area.name))
        return redirect('areasList')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editArea(request, pk):
    context = getViewContext()
    area = Area.objects.get(pk=pk)
    context['area'] = area
    if request.method == 'POST':
        name = request.POST.get('name')
        abbreviation = request.POST.get('abv')
        try:
            validateString(name, 'Nombre Área Docente')
            validateString(abbreviation, 'Abreviación')
            area.name = name
            area.abbreviation = abbreviation
            area.save()
            messages.success(request, getEditedSuccessMessage('Área Docente', name))
            return redirect('areasList')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Área Docente', name))
            return render(request, 'panel/univesityStuff/area/addOrEditArea.html', context)
        except Exception as e:
            messages.error(request, e.args[0])
            return render(request, 'panel/univesityStuff/area/addOrEditArea.html', context)
    return render(request, 'panel/univesityStuff/area/addOrEditArea.html', context)
