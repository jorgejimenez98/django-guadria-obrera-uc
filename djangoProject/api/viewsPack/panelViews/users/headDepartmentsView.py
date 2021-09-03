from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles import extra as ex
from ....helpFiles.decorators import checkUserAccess
from ....model.area.department import Department
from ....model.typeOfUsers.departmentHead import DepartmentHead


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'headDepartmentList': DepartmentHead.objects.all().order_by('-pk'),
        'usersList': [i for i in User.objects.all() if not i.groups.filter(name='Jefe Departamento').exists()],
        'departmentList': Department.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def headDepartmentsUsersList(request):
    return render(request, 'panel/users/headDepartments/headDepartmentsList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addHeadDepartmentUser(request):
    context = getViewContext()
    context['headDepartment'] = None
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        department = Department.objects.get(pk=int(request.POST.get('department')))
        try:
            user.groups.remove([i for i in user.groups.all()][0])
            user.groups.add(Group.objects.get(name='Jefe Departamento'))
            user.save()
            DepartmentHead.objects.create(
                user=user,
                department=department,
            )
            messages.success(request, ex.getAddedSuccessMessage('Usuario Jefe de Departamento', user.username))
            return redirect('headDepartmentsUsersList')
        except IntegrityError:
            messages.error(request, ex.getHDIntegrityErrorSMS('Jefe de Departamento', department.name, user.username))
    return render(request, 'panel/users/headDepartments/addOrEditHeadDepartments.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editHeadDepartmentUser(request, pk):
    context = getViewContext()
    oldDepartmentHead = DepartmentHead.objects.get(pk=pk)
    context['headDepartment'] = oldDepartmentHead
    if request.method == 'POST':
        user = User.objects.get(pk=int(request.POST.get('user')))
        department = Department.objects.get(pk=int(request.POST.get('department')))
        try:
            oldDepartmentHead.user.groups.remove([i for i in oldDepartmentHead.user.groups.all()][0])
            user.groups.remove([i for i in user.groups.all()][0])
            oldDepartmentHead.user.groups.add(Group.objects.get(name='Estudiante-Trabajador'))
            user.groups.add(Group.objects.get(name='Jefe Departamento'))

            oldDepartmentHead.user.save()
            user.save()

            oldDepartmentHead.user = user
            oldDepartmentHead.department = department
            oldDepartmentHead.save()
            messages.success(request, ex.getEditedSuccessMessage('Usuario Jede de Departamento', user.username))
            return redirect('headDepartmentsUsersList')
        except IntegrityError:
            messages.error(request, ex.getHDIntegrityErrorSMS('Jefe de Departamento', department.name, user.username))
    return render(request, 'panel/users/headDepartments/addOrEditHeadDepartments.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def changeHeadDepartmentUserRol(request, pk):
    context = getViewContext()
    departmentHead = DepartmentHead.objects.get(pk=pk)
    context['headDepartment'] = departmentHead
    try:
        departmentHead.user.groups.remove([i for i in departmentHead.user.groups.all()][0])
        departmentHead.user.groups.add(Group.objects.get(name='Estudiante-Trabajador'))
        departmentHead.user.save()
        departmentHead.delete()
        messages.success(request, ex.getRolChangedSuccessMessage('Jefe de Departamento', departmentHead.user.username))
        return redirect('headDepartmentsUsersList')
    except Exception as e:
        messages.error(request, e.args[0])
        return render(request, 'panel/users/headDepartments/addOrEditHeadDepartments.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteHeadDepartmentUser(request, pk):
    departmentHead = DepartmentHead.objects.get(pk=pk)
    try:
        user = User.objects.get(pk=departmentHead.user.pk)
        departmentHead.delete()
        user.delete()
        messages.success(request, ex.getEliminateSuccessMessage('Jefe de Departamento', departmentHead.user.username))
    except ProtectedError:
        messages.error(request, ex.getEliminateProtectErrorMessage('Jefe de Departamento', departmentHead.user.username))
    return redirect('headDepartmentsUsersList')
