from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.decorators import checkUserAccess
from ....model.person.sourceOfIncome import SourceOfIncome
from ....helpFiles.extra import *


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'sourceOfIncomesList': SourceOfIncome.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def allSourceIncomes(request):
    return render(request, 'panel/studentsStuff/sourceOfIncome/sourceOfIncomeList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addSourceOfIncome(request):
    context = getViewContext()
    context['sourceOfIncome'] = None
    if request.method == 'POST':
        sourceOfIncomeName = request.POST.get('name')
        try:
            validateString(sourceOfIncomeName, 'Fuente de Ingreso')
            SourceOfIncome.objects.create(name=sourceOfIncomeName)
            messages.success(request, getAddedSuccessMessage('Fuente de Ingreso', sourceOfIncomeName))
            return redirect('allSourceIncomes')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Fuente de Ingreso', sourceOfIncomeName))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/sourceOfIncome/addOrEditSourceOfIncome.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteSourceOfIncome(request, pk):
    sourceOfIncome = SourceOfIncome.objects.get(pk=pk)
    try:
        sourceOfIncome.delete()
        messages.success(request, getEliminateSuccessMessage('Fuente de Ingreso', sourceOfIncome.name))
    except ProtectedError:
        messages.error(request, getEliminateProtectErrorMessage('Fuente de Ingreso', sourceOfIncome.name))
    return redirect('allSourceIncomes')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editSourceOfIncome(request, pk):
    context = getViewContext()
    sourceOfIncome = SourceOfIncome.objects.get(pk=pk)
    context['sourceOfIncome'] = sourceOfIncome
    if request.method == 'POST':
        sourceOfIncomeName = request.POST.get('name')
        try:
            validateString(sourceOfIncomeName, 'Fuente de Ingreso')
            sourceOfIncome.name = sourceOfIncomeName
            sourceOfIncome.save()
            messages.success(request, getEditedSuccessMessage('Fuente de Ingreso', sourceOfIncomeName))
            return redirect('allSourceIncomes')
        except IntegrityError:
            messages.error(request, getUniqueErrorMessage('Fuente de Ingreso', sourceOfIncomeName))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/sourceOfIncome/addOrEditSourceOfIncome.html', context)
