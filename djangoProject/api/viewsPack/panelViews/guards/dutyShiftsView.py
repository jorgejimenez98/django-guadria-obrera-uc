from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....model.guard.dutyShift import DutyShift
from ....helpFiles import extra as ex


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'dutyShiftList': DutyShift.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
def dutyShiftsView(request):
    return render(request, 'panel/guardsStuff/dutyShifts/dutyShiftsList.html', getViewContext())


@login_required(login_url='/')
def addDutyShift(request):
    context = getViewContext()
    context['dutyShift']: None
    if request.method == 'POST':
        schedule = request.POST.get('schedule')
        try:
            ex.validateEmptyString(schedule, 'Horario')
            DutyShift.objects.create(schedule=schedule)
            messages.success(request, ex.getAddedSuccessMessage('Turno de Guardia', schedule))
            return redirect('dutyShiftsView')
        except IntegrityError:
            messages.error(request, ex.getUniqueErrorMessage('Turno de Guardia', schedule))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/guardsStuff/dutyShifts/dutyShiftAdd.html', context)


@login_required(login_url='/')
def editDutyShift(request, pk):
    dutyShit = DutyShift.objects.get(pk=pk)
    context = getViewContext()
    context['dutyShift'] = dutyShit
    if request.method == 'POST':
        schedule = request.POST.get('schedule')
        try:
            ex.validateEmptyString(schedule, 'Horario')
            dutyShit.schedule = schedule
            dutyShit.save()
            messages.success(request, ex.getAddedSuccessMessage('Turno de Guardia', schedule))
            return redirect('dutyShiftsView')
        except IntegrityError:
            messages.error(request, ex.getUniqueErrorMessage('Turno de Guardia', schedule))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/guardsStuff/dutyShifts/dutyShiftAdd.html', context)


@login_required(login_url='/')
def deleteDutyShift(request, pk):
    dutyShift = DutyShift.objects.get(id=pk)
    try:
        dutyShift.delete()
        messages.success(request, ex.getEliminateSuccessMessage('Turno de Guardia', dutyShift.schedule))
    except ProtectedError:
        messages.error(request, ex.getEliminateProtectErrorMessage('Turno de Guardia', dutyShift.schedule))
    except Exception as e:
        messages.error(request, e.args[0])
    return redirect('dutyShiftsView')
