from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles import extra as ex
from ....helpFiles.decorators import checkUserAccess
from ....model.area.career import Career
from ....model.typeOfUsers.ppaa import PPAA


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'ppaaList': PPAA.objects.all().order_by('-pk'),
        'usersList': [i for i in User.objects.all() if not i.groups.filter(name='PPAA').exists()],
        'careersList': Career.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def ppaaUsersList(request):
    return render(request, 'panel/users/ppaa/ppaaList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addPPAAUser(request):
    context = getViewContext()
    context['ppaa'] = None
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        career = Career.objects.get(pk=int(request.POST.get('career')))
        yearOfStudy = int(request.POST.get('yearOfStudy'))
        try:
            user.groups.remove([i for i in user.groups.all()][0])
            user.groups.add(Group.objects.get(name='PPAA'))
            user.save()
            PPAA.objects.create(
                user=user,
                career=career,
                yearOfStudy=yearOfStudy,
            )
            messages.success(request, ex.getAddedSuccessMessage('Usuario PPAA', user.username))
            return redirect('ppaaUsersList')
        except IntegrityError:
            messages.error(request, ex.getPPAAIntegrityErrorMessage('PPAA', career.name, user.username, yearOfStudy))
    return render(request, 'panel/users/ppaa/addOrEditPPAA.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editPPAAUser(request, pk):
    context = getViewContext()
    oldPPAA = PPAA.objects.get(pk=pk)
    context['ppaa'] = oldPPAA
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        career = Career.objects.get(pk=int(request.POST.get('career')))
        yearOfStudy = int(request.POST.get('yearOfStudy'))
        try:
            oldPPAA.user.groups.remove([i for i in oldPPAA.user.groups.all()][0])
            user.groups.remove([i for i in user.groups.all()][0])
            oldPPAA.user.groups.add(Group.objects.get(name='Estudiante-Trabajador'))
            user.groups.add(Group.objects.get(name='PPAA'))

            oldPPAA.user.save()
            user.save()

            oldPPAA.user = user
            oldPPAA.career = career
            oldPPAA.yearOfStudy = yearOfStudy
            oldPPAA.save()
            messages.success(request, ex.getAddedSuccessMessage('Usuario PPAA', user.username))
            return redirect('ppaaUsersList')
        except IntegrityError:
            messages.error(request, ex.getPPAAIntegrityErrorMessage('PPAA', career.name, user.username, yearOfStudy))
    return render(request, 'panel/users/ppaa/addOrEditPPAA.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def changePPAAUserRol(request, pk):
    context = getViewContext()
    ppaa = PPAA.objects.get(pk=pk)
    context['ppaa'] = ppaa
    try:
        ppaa.user.groups.remove([i for i in ppaa.user.groups.all()][0])
        ppaa.user.groups.add(Group.objects.get(name='Estudiante-Trabajador'))
        ppaa.user.save()
        ppaa.delete()
        messages.success(request, ex.getRolChangedSuccessMessage('PPAA', ppaa.user.username))
        return redirect('ppaaUsersList')
    except Exception as e:
        messages.error(request, e.args[0])
        return render(request, 'panel/users/ppaa/addOrEditPPAA.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deletePPAAUser(request, pk):
    ppaa = PPAA.objects.get(pk=pk)
    try:
        user = User.objects.get(pk=ppaa.user.pk)
        ppaa.delete()
        user.delete()
        messages.success(request, ex.getEliminateSuccessMessage('PPAA', ppaa.user.username))
    except ProtectedError:
        messages.error(request, ex.getEliminateProtectErrorMessage('PPAA', ppaa.user.username))
    return redirect('ppaaUsersList')
