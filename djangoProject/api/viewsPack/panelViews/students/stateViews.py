from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles import extra as extra
from ....helpFiles.decorators import checkUserAccess
from ....model.person.state import State


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'statesList': State.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def statesList(request):
    return render(request, 'panel/state/stateList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addState(request):
    context = getViewContext()
    context['state'] = None
    if request.method == 'POST':
        name = request.POST.get('name')
        typeOfPerson = request.POST.get('typeOfPerson')
        try:
            extra.validateString(name, 'Nombre del Estado')
            extra.validateString(typeOfPerson, 'Tipo de Persona')
            State.objects.create(name=request.POST.get('name'), typeOfPerson=typeOfPerson)
            messages.success(request, extra.getAddedSuccessMessage('Estado', f'{name}-{typeOfPerson}'))
            return redirect('statesList')
        except IntegrityError:
            messages.error(request, extra.getUniqueErrorMessage('Estado', name))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/state/addOrEditState.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteState(request, pk):
    state = State.objects.get(pk=pk)
    try:
        state.delete()
        messages.success(request, extra.getEliminateSuccessMessage('Estado', state.name))
    except ProtectedError:
        messages.error(request, extra.getEliminateProtectErrorMessage('Estado', state.name))
    return redirect('statesList')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editState(request, pk):
    context = getViewContext()
    state = State.objects.get(pk=pk)
    context['state'] = state
    if request.method == 'POST':
        name = request.POST.get('name')
        typeOfPerson = request.POST.get('typeOfPerson')
        try:
            extra.validateString(name, 'Nombre del Estado')
            extra.validateString(typeOfPerson, 'Tipo de Persona')
            state.name = name
            state.typeOfPerson = typeOfPerson
            state.save()
            messages.success(request, extra.getEditedSuccessMessage('Estado', name))
            return redirect('statesList')
        except IntegrityError:
            messages.error(request, extra.getUniqueErrorMessage('Estado', name))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/state/addOrEditState.html', context)
