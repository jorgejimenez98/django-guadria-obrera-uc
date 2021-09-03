from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.decorators import checkUserAccess
from ....model.area.area import Area
from ....model.area.department import Department
from ....helpFiles.extra import *


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'departmentsList': Department.objects.all().order_by('-pk'),
        'areasList': Area.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def departmentsList(request):
    return render(request, 'panel/univesityStuff/departments/departmentsList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addDepartment(request):
    context = getViewContext()
    context['department'] = None
    if request.method == 'POST':
        name = request.POST.get('name')
        areaName = request.POST.get('areaName')
        try:
            validateString(name, 'Departamento')
            validateSelectString(areaName, 'Área Docente')
            newArea = Area.objects.get(pk=int(areaName))
            Department.objects.create(name=name, area=newArea)
            messages.success(request, getAddedSuccessMessage('Departamento', newArea.name))
            return redirect('departmentsList')
        except IntegrityError:
            messages.error(request, getDoubleIntegrityErrorMessage('Departamento', name, 'Área Docente', areaName))
            return render(request, 'panel/univesityStuff/departments/addOrEditDepartment.html', context)
        except Exception as e:
            messages.error(request, e.args[0])
            return render(request, 'panel/univesityStuff/departments/addOrEditDepartment.html', context)
    return render(request, 'panel/univesityStuff/departments/addOrEditDepartment.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteDepartment(request, pk):
    department = Department.objects.get(pk=pk)
    try:
        department.delete()
        messages.success(request, getEliminateSuccessMessage('Departamento', department.name))
        return redirect('departmentsList')
    except ProtectedError:
        messages.error(request, getEliminateProtectErrorMessage('Departamento', department.name))
        return redirect('departmentsList')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editDepartment(request, pk):
    context = getViewContext()
    department = Department.objects.get(pk=pk)
    context['department'] = department
    if request.method == 'POST':
        name = request.POST.get('name')
        areaName = request.POST.get('areaName')
        try:
            validateString(name, 'Departamento')
            validateSelectString(areaName, 'Área Docente')
            department.name = name
            department.area = Area.objects.get(pk=int(areaName))
            department.save()
            messages.success(request, getEditedSuccessMessage('Departamento', name))
            return redirect('departmentsList')
        except IntegrityError:
            messages.error(request, getDoubleIntegrityErrorMessage('Departamento', name, 'Área Docente', areaName))
            return render(request, 'panel/univesityStuff/departments/addOrEditDepartment.html', context)
        except Exception as e:
            messages.error(request, e.args[0])
            return render(request, 'panel/univesityStuff/departments/addOrEditDepartment.html', context)
    return render(request, 'panel/univesityStuff/departments/addOrEditDepartment.html', context)
