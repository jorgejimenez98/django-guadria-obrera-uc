from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ....helpFiles.decorators import checkUserAccess
from ....model.area.universitySeat import UniversitySeat
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles import extra as ex


def getViewContext():
    context = {
        'seatList': UniversitySeat.objects.all().order_by('-pk'),
        'today': getTodayDayOnACompleteString(),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def universitySeatList(request):
    return render(request, 'panel/univesityStuff/universitySeat/universitySeatList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addUniversitySeat(request):
    context = getViewContext()
    context['seat'] = None
    if request.method == 'POST':
        seat = request.POST.get('name')
        cantAOGS = request.POST.get('cantAOGS')
        try:
            ex.validateString(seat, 'Nombre Sede')
            UniversitySeat.objects.create(
                name=seat,
                AOGS_Cuantity=int(cantAOGS)
            )
            messages.success(request, ex.getAddedSuccessMessage('Sede Universitaria', seat))
            return redirect('universitySeatList')
        except IntegrityError:
            messages.error(request, ex.getUniqueErrorMessage('Sede Universitaria', seat))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/univesityStuff/universitySeat/addOrEditUniversitySeat.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteUniversitySeat(request, pk):
    seat = UniversitySeat.objects.get(pk=pk)
    try:
        seat.delete()
        messages.success(request, ex.getEliminateSuccessMessage('Sede Universitaria', seat.name))
    except ProtectedError:
        messages.error(request, ex.getEliminateProtectErrorMessage('Sede Universitaria', seat.name))
    return redirect('universitySeatList')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editUniversitySeat(request, pk):
    seat = UniversitySeat.objects.get(pk=pk)
    context = getViewContext()
    context['seat'] = seat
    if request.method == 'POST':
        seatName = request.POST.get('name')
        cantOAGS = request.POST.get('cantAOGS')
        try:
            ex.validateString(seatName, 'Nombre Sede')
            seat.name = seatName
            seat.AOGS_Cuantity = cantOAGS
            seat.save()
            messages.success(request, ex.getEditedSuccessMessage('Sede Universitaria', seat.name))
            return redirect('universitySeatList')
        except IntegrityError:
            messages.error(request, ex.getUniqueErrorMessage(seat, 'Sede Universitaria'))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/univesityStuff/universitySeat/addOrEditUniversitySeat.html', context)
