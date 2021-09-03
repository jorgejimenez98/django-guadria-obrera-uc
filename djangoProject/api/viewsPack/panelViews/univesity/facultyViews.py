from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.decorators import checkUserAccess
from ....model.area.faculty import Faculty
from ....helpFiles.extra import *


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'facultyList': Faculty.objects.all().order_by('-pk'),
        'facultyListLength': Faculty.objects.all().count(),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def facultyList(request):
    return render(request, 'panel/univesityStuff/faculty/facultyList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addFaculty(request):
    context = getViewContext()
    context['faculty'] = None
    if request.method == 'POST':
        name = request.POST.get('name')
        abbreviation = request.POST.get('abv')
        try:
            validateString(name, 'Nombre Facultad')
            validateString(abbreviation, 'Abreviación')
            Faculty.objects.create(name=name, abbreviation=abbreviation)
            messages.success(request, getAddedSuccessMessage('Facultad', name))
            return redirect('facultyList')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Facultad', name))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/univesityStuff/faculty/addOrEditFaculty.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteFaculty(request, pk):
    faculty = Faculty.objects.get(pk=pk)
    try:
        faculty.delete()
        messages.success(request, getEliminateSuccessMessage('Facultad', faculty.name))
    except ProtectedError:
        messages.error(request, getEliminateProtectErrorMessage('Facultad', faculty.name))
    return redirect('facultyList')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editFaculty(request, pk):
    context = getViewContext()
    faculty = Faculty.objects.get(pk=pk)
    context['faculty'] = faculty
    if request.method == 'POST':
        name = request.POST.get('name')
        abbreviation = request.POST.get('abv')
        try:
            validateString(name, 'Nombre Facultad')
            validateString(abbreviation, 'Abreviación')
            faculty.name = name
            faculty.abbreviation = abbreviation
            faculty.save()
            messages.success(request, getEditedSuccessMessage('Facultad', name))
            return redirect('facultyList')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Facultad', name))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/univesityStuff/faculty/addOrEditFaculty.html', context)
