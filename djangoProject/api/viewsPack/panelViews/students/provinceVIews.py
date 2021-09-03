from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ....helpFiles.decorators import checkUserAccess
from ....model.person.province import Province
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.extra import *


def getViewContext():
    context = {
        'provinceList': Province.objects.all(),
        'today': getTodayDayOnACompleteString(),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def provinceView(request):
    return render(request, 'panel/studentsStuff/province/provinceList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addProvince(request):
    context = getViewContext()
    context['province'] = None
    if request.method == 'POST':
        provinceName = request.POST.get('province')
        try:
            validateString(provinceName, 'Nombre de Provincia')
            Province.objects.create(name=provinceName)
            messages.success(request, getAddedSuccessMessage('Nombre de Provincia', provinceName))
            return redirect('provinceView')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Nombre de Provincia', provinceName))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/province/addProvince.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteProvince(request, pk):
    provinceToDelete = Province.objects.get(pk=pk)
    try:
        provinceToDelete.delete()
        messages.success(request, getEliminateSuccessMessage('Provincia', provinceToDelete.name))
    except ProtectedError:
        messages.error(request, getEliminateProtectErrorMessage('Provincia', provinceToDelete.name))
    return redirect('provinceView')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editProvince(request, pk):
    province = Province.objects.get(pk=pk)
    context = getViewContext()
    context['province'] = province
    if request.method == 'POST':
        provinceName = request.POST.get('province')
        try:
            validateString(provinceName, 'Nombre de Provincia')
            province.name = provinceName
            messages.success(request, getAddedSuccessMessage('Nombre de Provincia', provinceName))
            return redirect('provinceView')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Nombre de Provincia', provinceName))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/province/addProvince.html', context)
