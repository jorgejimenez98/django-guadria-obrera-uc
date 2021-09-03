from django.shortcuts import render

from api.helpFiles.dateFunctions import getTodayDayOnACompleteString
from api.model.guard.guard import Guard
from api.model.guard.studentsGuard import StudentsGuard
from api.model.guard.workersGuard import WorkersGuard

def guardByUniversitySeatView(request, pk):
    actualGuard = Guard.objects.get(pk=pk)
    studentsGuard = StudentsGuard.objects.all().filter(guard=actualGuard)
    workersGuard = WorkersGuard.objects.all().filter(guard=actualGuard)
    context = {
        'guard': actualGuard,
        'today': getTodayDayOnACompleteString()
    }
    return render(request, 'public/guardByUniversitySeat.html', context)

    # for i in studentsGuard.all():
    #     print(i)
    # print('\n' + 'ok' * 20)
    # for i in workersGuard.all():
    #     print(i)
