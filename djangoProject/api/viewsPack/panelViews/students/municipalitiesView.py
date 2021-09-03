from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ....model.person.municipality import Municipality, Province
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.decorators import checkUserAccess
from ....helpFiles import extra as ex


def getViewContext():
    context = {
        'municipalityList': Municipality.objects.all().order_by('-pk'),
        'provinces': Province.objects.all(),
        'today': getTodayDayOnACompleteString(),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def municipalitiesView(request):
    return render(request, 'panel/studentsStuff/municipalities/municipalitiesList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addMunicipality(request):
    context = getViewContext()
    context['municipality'] = None
    if request.method == 'POST':
        name = request.POST.get('municipality')
        provinceID = request.POST.get('provinceOption')
        try:
            ex.validateString(name, 'Nombre Municipio')
            ex.validateSelectString(provinceID, 'Provincia')
            Municipality.objects.create(
                name=name,
                province=Province.objects.get(id=int(provinceID))
            )
            messages.success(request, ex.getAddedSuccessMessage('Municipio', name))
            return redirect('municipalitiesView')
        except IntegrityError:
            sms = ex.getDoubleIntegrityErrorMessage('Municipio', name, 'Provincia', Province.objects.get(pk=int(provinceID)).name)
            messages.error(request, sms)
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/municipalities/municipalitiesAdd.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteMunicipality(request, pk):
    municipality = Municipality.objects.get(pk=pk)
    try:
        municipality.delete()
        messages.success(request, ex.getEliminateSuccessMessage('Municipio', municipality.name))
    except ProtectedError:
        messages.error(request, ex.getEliminateProtectErrorMessage('Municipio', municipality.name))
    return redirect('municipalitiesView')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editMunicipality(request, pk):
    municipality = Municipality.objects.get(pk=pk)
    context = getViewContext()
    context['municipality'] = municipality
    if request.method == 'POST':
        name = request.POST.get('municipality')
        provinceID = request.POST.get('provinceOption')
        try:
            ex.validateString(name, 'Nombre Municipio')
            ex.validateSelectString(provinceID, 'Provincia')
            municipality.name = name
            municipality.province = Province.objects.get(pk=int(provinceID))
            municipality.save()
            messages.success(request, ex.getEditedSuccessMessage('Municipio', name))
            return redirect('municipalitiesView')
        except IntegrityError:
            sms = ex.getDoubleIntegrityErrorMessage('Municipio', name, 'Provincia', Province.objects.get(pk=int(provinceID)).name)
            messages.error(request, sms)
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/municipalities/municipalitiesAdd.html', context)
