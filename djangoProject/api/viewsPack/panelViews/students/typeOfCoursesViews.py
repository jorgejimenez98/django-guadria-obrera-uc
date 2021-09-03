from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles.decorators import checkUserAccess
from ....model.person.typeOfCourse import TypeOfCourse
from ....helpFiles import extra as extra


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'typeOfCoursesList': TypeOfCourse.objects.all(),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def allTypeOfCourses(request):
    return render(request, 'panel/studentsStuff/typeOfCourses/typeOfCourseList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addTypeOfCourse(request):
    context = getViewContext()
    context['typeOfCourse'] = None
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            extra.validateString(name, 'Nombre del Tipo de Curso')
            TypeOfCourse.objects.create(name=name)
            messages.success(request, extra.getAddedSuccessMessage('Tipo de Curso', name))
            return redirect('allTypeOfCourses')
        except IntegrityError:
            messages.error(request, extra.getUniqueErrorMessage('Tipo de Curso', name))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/typeOfCourses/addOrEditTypeOfCourse.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteTypeOfCourse(request, pk):
    typeOfCourse = TypeOfCourse.objects.get(pk=pk)
    try:
        typeOfCourse.delete()
        messages.success(request, extra.getEliminateSuccessMessage('Tipo de Curso', typeOfCourse.name))
        return redirect('allTypeOfCourses')
    except ProtectedError:
        messages.error(request, extra.getEliminateProtectErrorMessage('Tipo de Curso', typeOfCourse.name))
        return redirect('allTypeOfCourses')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editTypeOfCourse(request, pk):
    context = getViewContext()
    typeOfCourse = TypeOfCourse.objects.get(pk=pk)
    context['typeOfCourse'] = typeOfCourse
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            extra.validateString(name, 'Nombre del Tipo de Curso')
            typeOfCourse.name = name
            typeOfCourse.save()
            messages.success(request, extra.getEditedSuccessMessage('Tipo de Curso', name))
            return redirect('allTypeOfCourses')
        except IntegrityError:
            messages.error(request, extra.getUniqueErrorMessage('Tipo de Curso', name))
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/studentsStuff/typeOfCourses/addOrEditTypeOfCourse.html', context)
