from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles import extra as ex
from ....helpFiles.decorators import checkUserAccess
from ....model.area.faculty import Faculty
from ....model.typeOfUsers.dean import Dean


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'deanList': Dean.objects.all().order_by('-pk'),
        'usersList': [i for i in User.objects.all() if not i.groups.filter(name='Decano').exists()],
        'facultyList': Faculty.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deanUsersList(request):
    return render(request, 'panel/users/dean/deanUsersList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addDeanUser(request):
    context = getViewContext()
    context['dean'] = None
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        faculty = Faculty.objects.get(pk=int(request.POST.get('faculty')))
        try:
            user.groups.remove([i for i in user.groups.all()][0])
            user.groups.add(Group.objects.get(name='Decano'))
            user.save()
            Dean.objects.create(
                user=user,
                faculty=faculty,
            )
            messages.success(request, ex.getAddedSuccessMessage('Usuario Decano', user.username))
            return redirect('deanUsersList')
        except IntegrityError:
            messages.error(request, ex.getDeanIntegrityErrorMessage('Decano', faculty.name, user.username))
    return render(request, 'panel/users/dean/addOrEditDeanUser.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editDeanUser(request, pk):
    context = getViewContext()
    oldDean = Dean.objects.get(pk=pk)
    context['dean'] = oldDean
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        faculty = Faculty.objects.get(pk=int(request.POST.get('faculty')))
        try:
            oldDean.user.groups.remove([i for i in oldDean.user.groups.all()][0])
            user.groups.remove([i for i in user.groups.all()][0])
            oldDean.user.groups.add(Group.objects.get(name='Estudiante-Trabajador'))
            user.groups.add(Group.objects.get(name='Decano'))

            oldDean.user.save()
            user.save()

            oldDean.user = user
            oldDean.faculty = faculty
            oldDean.save()
            messages.success(request, ex.getEditedSuccessMessage('Usuario Decano', user.username))
            return redirect('deanUsersList')
        except IntegrityError:
            messages.error(request, ex.getDeanIntegrityErrorMessage('Decano', faculty.name, user.username))
    return render(request, 'panel/users/dean/addOrEditDeanUser.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def changeDeanUserRol(request, pk):
    context = getViewContext()
    dean = Dean.objects.get(pk=pk)
    context['dean'] = dean
    try:
        dean.user.groups.remove([i for i in dean.user.groups.all()][0])
        dean.user.groups.add(Group.objects.get(name='Estudiante-Trabajador'))
        dean.user.save()
        dean.delete()
        messages.success(request, ex.getRolChangedSuccessMessage('Decano', dean.user.username))
        return redirect('deanUsersList')
    except Exception as e:
        messages.error(request, e.args[0])
        return render(request, 'panel/users/dean/addOrEditDeanUser.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteDeanUser(request, pk):
    deann = Dean.objects.get(pk=pk)
    try:
        user = User.objects.get(pk=deann.user.pk)
        deann.delete()
        user.delete()
        messages.success(request, ex.getEliminateSuccessMessage('Decano', deann.user.username))
    except ProtectedError:
        messages.error(request, ex.getEliminateProtectErrorMessage('Decano', deann.user.username))
    return redirect('deanUsersList')
