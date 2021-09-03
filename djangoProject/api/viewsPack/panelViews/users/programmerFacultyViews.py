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
from ....model.typeOfUsers.facultyProgrammer import FacultyProgrammer


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'programmerFacultyList': FacultyProgrammer.objects.all().order_by('-pk'),
        'usersList': [i for i in User.objects.all() if not i.groups.filter(name='Programador Facultad').exists()],
        'facultyList': Faculty.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def programmerFacultyUsersList(request):
    return render(request, 'panel/users/facultyProgrammer/facultyProgrammerList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addProgrammerFacultyUser(request):
    context = getViewContext()
    context['facultyProgrammer'] = None
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        faculty = Faculty.objects.get(pk=int(request.POST.get('faculty')))
        try:
            user.groups.remove(Group.objects.get(name='Programador Facultad'))
            user.groups.add(Group.objects.get(name='Programador Facultad'))
            user.save()
            FacultyProgrammer.objects.create(
                user=user,
                faculty=faculty,
            )
            messages.success(request, ex.getAddedSuccessMessage('Programador de la Guardia', user.username))
            return redirect('programmerFacultyUsersList')
        except IntegrityError:
            errorMessage = ex.getPFIntegrityErrorMessage('Programador de la Guardia', faculty.name, user.username)
            messages.error(request, errorMessage)
    return render(request, 'panel/users/facultyProgrammer/addOrEditFacultyProgrammer.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editProgrammerFacultyUser(request, pk):
    context = getViewContext()
    facultyProgrammer = FacultyProgrammer.objects.get(pk=pk)
    context['facultyProgrammer'] = facultyProgrammer
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        faculty = Faculty.objects.get(pk=int(request.POST.get('faculty')))
        try:
            facultyProgrammer.user.groups.remove([i for i in facultyProgrammer.user.groups.all()][0])
            user.groups.remove(Group.objects.get(name='Programador Facultad'))
            facultyProgrammer.user.groups.add(Group.objects.get(name='Estudiante-Trabajador'))
            user.groups.add(Group.objects.get(name='Programador Facultad'))

            facultyProgrammer.user.save()
            user.save()

            facultyProgrammer.user = user
            facultyProgrammer.faculty = faculty
            facultyProgrammer.save()
            messages.success(request, ex.getEditedSuccessMessage('Programador de la Guardia', user.username))
            return redirect('programmerFacultyUsersList')
        except IntegrityError:
            errorMessage = ex.getDeanIntegrityErrorMessage('Programador de la Guardia', faculty.name, user.username)
            messages.error(request, errorMessage)
    return render(request, 'panel/users/facultyProgrammer/addOrEditFacultyProgrammer.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def changeProgrammerFacultyUserRol(request, pk):
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
def deleteProgrammerFacultyUser(request, pk):
    deann = Dean.objects.get(pk=pk)
    try:
        user = User.objects.get(pk=deann.user.pk)
        deann.delete()
        user.delete()
        messages.success(request, ex.getEliminateSuccessMessage('Decano', deann.user.username))
    except ProtectedError:
        messages.error(request, ex.getEliminateProtectErrorMessage('Decano', deann.user.username))
    return redirect('deanUsersList')
