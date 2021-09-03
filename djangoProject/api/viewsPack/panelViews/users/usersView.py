from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles import extra as ex
from ....helpFiles.decorators import checkUserAccess


def getViewContext():
    context = {
        'today': getTodayDayOnACompleteString(),
        'usersList': User.objects.all().order_by('-pk'),
    }
    return context


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def usersList(request):
    return render(request, 'panel/users/normalUsers/usersList.html', getViewContext())


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def addUser(request):
    context = getViewContext()
    context['user'] = None
    if request.method == 'POST':
        username = request.POST.get('username')
        firstName = request.POST.get('names')
        lastNames = request.POST.get('lastNames')
        email = request.POST.get('email')
        password = request.POST.get('password')
        groupName = request.POST.get('rol')
        try:
            newUser = User.objects.create(
                username=username,
                first_name=firstName,
                last_name=lastNames,
                email=email,
            )
            newUser.set_password(password)
            newUser.groups.add(Group.objects.get(name=groupName))
            newUser.save()
            messages.success(request, ex.getAddedSuccessMessage('Usuario', f'{firstName} - {lastNames} - ({username})'))
            return redirect('usersList')
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/users/normalUsers/addOrEditUser.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def deleteUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        messages.success(request, ex.getEliminateSuccessMessage('Usuario', user.username))
        return redirect('usersList')
    except Exception as e:
        messages.error(request, e.args[0])
        return redirect('usersList')


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def editUser(request, pk):
    context = getViewContext()
    oldUser = User.objects.get(pk=pk)
    context['user'] = oldUser
    if request.method == 'POST':
        username = request.POST.get('username')
        firstName = request.POST.get('names')
        lastNames = request.POST.get('lastNames')
        try:
            oldUser.username = username
            oldUser.first_name = firstName
            oldUser.last_name = lastNames
            oldUser.email = request.POST.get('email')
            oldUser.groups.add(Group.objects.get(name=Group.objects.get(name=request.POST.get('rol'))))
            oldUser.save()
            messages.success(request, ex.getEditedSuccessMessage('Usuario', f'{firstName} - {lastNames} - ({username})'))
            return redirect('usersList')
        except Exception as e:
            messages.error(request, e.args[0])
    return render(request, 'panel/users/normalUsers/addOrEditUser.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Administrador', login_url='/error403/')
def changeUserPassword(request, pk):
    context = getViewContext()
    user = User.objects.get(pk=pk)
    context['user'] = user
    if request.method == 'POST':
        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('password')
        if user.check_password(oldPassword):
            user.set_password(newPassword)
            user.save()
            messages.success(request, ex.getPasswordUpdatedSuccessMessage(user.username))
            return redirect('usersList')
        messages.error(request, ex.getIncorrectPasswordMessage(user.username))
    return render(request, 'panel/users/normalUsers/changePassword.html', context)
