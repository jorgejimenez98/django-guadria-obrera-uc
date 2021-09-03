from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def loginView(request):
    return render(request, 'login.html', {'error': False})


def logoutView(request):
    logout(request)
    return redirect('homeView')


def loginUserToTheSite(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('administrationPanelView')
        return render(request, 'login.html', {'error': True})
    return render(request, 'login.html', {'error': False})
