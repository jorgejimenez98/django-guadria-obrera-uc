from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from ....helpFiles import extra as extra
from ....helpFiles.decorators import checkUserAccess
from ....model.person.typeOfStudent import TypeOfStudent
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'typeOfStudentsList': TypeOfStudent.objects.all(),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def allTypeOfStudents(request):
    return render(request, 'panel/studentsStuff/typeOfStudents/typeOfStudentsList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addTypeOfStudent(request):
    context = getViewContext()
    context['typeOfStudent'] = None
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            extra.validateString(name, 'Nombre del Estado')
            TypeOfStudent.objects.create(name=request.POST.get('name'))
            messages.success(request, extra.getAddedSuccessMessage('Tipo de Estudiante', name))
            return redirect('allTypeOfStudents')
        except IntegrityError:
            messages.error(request, extra.getUniqueErrorMessage('Tipo de Estudiante', name))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/typeOfStudents/addOrEditTypeOfStudents.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteTypeOfStudent(request, pk):
    typeOfStudent = TypeOfStudent.objects.get(pk=pk)
    try:
        typeOfStudent.delete()
        messages.success(request, extra.getEliminateSuccessMessage('Tipo de Estudiante', typeOfStudent.name))
        return redirect('allTypeOfStudents')
    except ProtectedError:
        messages.error(request, extra.getEliminateProtectErrorMessage('Tipo de Estudiante', typeOfStudent.name))
        return redirect('allTypeOfStudents')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editTypeOfStudent(request, pk):
    context = getViewContext()
    typeOfStudent = TypeOfStudent.objects.get(pk=pk)
    context['typeOfStudent'] = typeOfStudent
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            extra.validateString(name, 'Nombre del Estado')
            typeOfStudent.name = name
            typeOfStudent.save()
            messages.success(request, extra.getEditedSuccessMessage('Tipo de Estudiante', name))
            return redirect('allTypeOfStudents')
        except IntegrityError:
            messages.error(request, extra.getUniqueErrorMessage('Tipo de Estudiante', name))
            return render(request, 'panel/studentsStuff/typeOfStudents/addOrEditTypeOfStudents.html', context)
        except Exception as e:
            messages.error(request, e.args[0])
            return render(request, 'panel/studentsStuff/typeOfStudents/addOrEditTypeOfStudents.html', context)
    return render(request, 'panel/studentsStuff/typeOfStudents/addOrEditTypeOfStudents.html', context)
