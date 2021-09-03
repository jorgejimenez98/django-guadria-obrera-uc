from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage


# Create your views here.
def contactView(request):
    if not request.user.is_authenticated:
        return render(request, 'public/conctactPage.html', {'error': None})
    return redirect('administrationPanelView')


def addNewContactMessage(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            typeOfPerson=request.POST.get('typeOfPerson'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return redirect('contactView')
    return redirect('contactView')
