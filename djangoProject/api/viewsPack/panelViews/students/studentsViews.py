from django.shortcuts import render
from api.helpFiles.dateFunctions import getTodayDayOnACompleteString


def studentsList(request):
    context = {
        'today': getTodayDayOnACompleteString()
    }
    return render(request, 'panel/studentsStuff/students/studentsList.html', context)
