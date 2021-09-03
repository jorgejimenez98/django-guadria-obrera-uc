from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from api.helpFiles.dateFunctions import getTodayDayOnACompleteString
from api.helpFiles.djangoFunctions import getPagination
from api.model.area.career import Career
from api.helpFiles.extra import *
from api.model.area.faculty import Faculty


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'careersList': Career.objects.all().order_by('-pk'),
        'careersListLength': Career.objects.all().count(),
        'facultyList': Faculty.objects.all(),
    }
    return context


@login_required(login_url='/')
def careersList(request):
    context = getViewContext()
    context['careersList'] = getPagination(request, context['careersList'], 10)
    return render(request, 'panel/univesityStuff/careers/careersList.html', context)


@login_required(login_url='/')
def addCareer(request):
    context = getViewContext()
    context['career'] = None
    if request.method == 'POST':
        name = request.POST.get('name')
        facultyId = request.POST.get('facultyName')
        try:
            validateString(name, 'Carrera')
            validateSelectString(facultyId, 'Facultad')
            faculty = Faculty.objects.get(pk=int(facultyId))
            Career.objects.create(name=name, faculty=faculty)
            messages.success(request, getAddedSuccessMessage('Carrera', name))
            return redirect('careersList')
        except IntegrityError:
            facultyName = Faculty.objects.get(pk=int(facultyId)).name
            messages.error(request, getDoubleIntegrityErrorMessage('Carrera', name, 'Facultad', facultyName))
            return render(request, 'panel/univesityStuff/careers/addOrEditCareer.html', context)
        except Exception as e:
            messages.error(request, e.args[0])
            return render(request, 'panel/univesityStuff/careers/addOrEditCareer.html', context)
    return render(request, 'panel/univesityStuff/careers/addOrEditCareer.html', context)


@login_required(login_url='/')
def deleteCareer(request, pk):
    career = Career.objects.get(pk=pk)
    try:
        career.delete()
        messages.success(request, getEliminateSuccessMessage('Carrera', career.name))
        return redirect('careersList')
    except ProtectedError:
        messages.error(request, getEliminateProtectErrorMessage('Carrera', career.name))
        return redirect('careersList')


@login_required(login_url='/')
def editCareer(request, pk):
    context = getViewContext()
    career = Career.objects.get(pk=pk)
    context['career'] = career
    if request.method == 'POST':
        name = request.POST.get('name')
        facultyId = request.POST.get('facultyName')
        try:
            validateString(name, 'Carrera')
            validateSelectString(facultyId, 'Facultad')
            career.name = name
            career.faculty = Faculty.objects.get(pk=int(facultyId))
            career.save()
            messages.success(request, getAddedSuccessMessage('Carrera', name))
            return redirect('careersList')
        except IntegrityError:
            facultyName = Faculty.objects.get(pk=int(facultyId)).name
            messages.error(request, getDoubleIntegrityErrorMessage('Carrera', name, 'Facultad', facultyName))
            return render(request, 'panel/univesityStuff/careers/addOrEditCareer.html', context)
        except Exception as e:
            messages.error(request, e.args[0])
            return render(request, 'panel/univesityStuff/careers/addOrEditCareer.html', context)
    return render(request, 'panel/univesityStuff/careers/addOrEditCareer.html', context)
