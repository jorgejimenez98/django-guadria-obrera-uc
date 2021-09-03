from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from ....helpFiles.dateFunctions import getTodayDayOnACompleteString
from ....helpFiles import extra
from ....helpFiles.decorators import checkUserAccess
from ....model.area.area import Area
from ....model.area.faculty import Faculty
from ....model.area.universitySeat import UniversitySeat
from ....model.officialDistributionOGS import OfficialDistributionOGS, getTodayDetails
from ....model.person.worker import Worker
from datetime import datetime
import django_excel as excel


def getAllAreasWithWorkers(universitySeat):
    areasArray = []
    officialDistributions = OfficialDistributionOGS.objects.filter(universitySeat__name=universitySeat)
    actualWorkers = [i.guardOfficer for i in officialDistributions]
    for i in Area.objects.all():
        if i.name not in areasArray:
            areasArray.append([i.name])
    for worker in Worker.objects.all():
        for i in areasArray:
            if worker.department.area.name == i[0] and worker not in actualWorkers:
                i.append(worker)
    return areasArray


def getTableViewContext(universitySeatAux):
    return {
        'today': getTodayDayOnACompleteString(),
        'universitySeat': universitySeatAux,
        'todayDay': datetime.today().day,
        'officialDistributions': OfficialDistributionOGS.objects.filter(
            universitySeat__name=universitySeatAux.name).order_by('dayOfMonth'),
    }


@login_required(login_url='/')
@checkUserAccess(rol='Programador UC', login_url='/error403/')
def officialDistributionOGS(request):
    context = {
        'today': getTodayDayOnACompleteString(),
        'joseMartiDetails': getTodayDetails(UniversitySeat.objects.get(pk=3).name),
        'agramonteDetails': getTodayDetails(UniversitySeat.objects.get(pk=2).name),
        'fajardoDetails': getTodayDetails(UniversitySeat.objects.get(pk=4).name),
    }
    return render(request, 'panel/guardsStuff/officialDistributionOGS/allOfficialDistributionOGS.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Programador UC', login_url='/error403/')
def officialOGSDistributionBySeatName(request, universitySeat):
    universitySeatAux = UniversitySeat.objects.get(name=universitySeat)
    context = getTableViewContext(universitySeatAux)
    return render(request, 'panel/guardsStuff/officialDistributionOGS/gestOfficialDistributionOGSBySeat.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Programador UC', login_url='/error403/')
def editOfficialOGSDistributionBySeatAndDayOfMonth(request, universitySeat, day):
    officialOGSlDistribution = OfficialDistributionOGS.objects.get(universitySeat__name=universitySeat, dayOfMonth=day)
    context = {
        'officialOGSlDistribution': officialOGSlDistribution,
        'today': getTodayDayOnACompleteString(),
        'workers': Worker.objects.all(),
        'areasWithWorkers': getAllAreasWithWorkers(universitySeat),
        'areaList': Area.objects.all(),
        'facultyList': Faculty.objects.all(),
    }
    if request.method == 'POST':
        workerValue = request.POST.get('ogsWorker')
        areaValue = request.POST.get('area')
        facultyValue = request.POST.get('faculty')
        newOGSWorker = None if workerValue == '' else Worker.objects.get(pk=workerValue)
        officialOGSlDistribution.guardOfficer = newOGSWorker
        officialOGSlDistribution.area = None if areaValue == '' else Area.objects.get(pk=int(areaValue))
        officialOGSlDistribution.faculty = None if facultyValue == '' else Faculty.objects.get(pk=int(facultyValue))
        tableContext = getTableViewContext(officialOGSlDistribution.universitySeat)
        try:
            officialOGSlDistribution.save()
            messages.success(request, extra.getOfficialDistributionUpdatedSuccessMessage('OGS', day))
            return render(request, 'panel/guardsStuff/officialDistributionOGS/gestOfficialDistributionOGSBySeat.html',
                          tableContext)
        except IntegrityError:
            context['message'] = 'Este OGS ({} {}) ya tiene un dia asignado para esta sede'.format(newOGSWorker.names,
                                                                                                   newOGSWorker.surnames)
    return render(request, 'panel/guardsStuff/officialDistributionOGS/editOGSOfficialDistribution.html', context)


@login_required(login_url='/')
@checkUserAccess(rol='Programador UC', login_url='/error403/')
def exportToExcel(request, universitySeat, fileType):
    export = [['Día', 'OGS', 'Área', 'Trabajadores', 'Alumnos']]
    guardDistributions = OfficialDistributionOGS.objects.filter(universitySeat__name=universitySeat).order_by(
        'dayOfMonth')
    for od in guardDistributions:
        newColumn = ['' for _ in range(5)]
        newColumn[0] = od.dayOfMonth
        newColumn[1] = 'NR' if not od.hasGuardOfficer else f'{od.guardOfficer.names} {od.guardOfficer.surnames}'
        newColumn[2] = 'NR' if not od.hasGuardOfficer else od.guardOfficer.department.area.name
        newColumn[3] = 'NR' if not od.hasArea else od.area.name
        newColumn[4] = 'NR' if not od.hasFaculty else od.faculty.name
        export.append(newColumn)
    strToday = datetime.now().strftime("%Y-%m-%d")
    sheet = excel.pe.Sheet(export)
    fileName = "DistribucionOficialOGS_Sede_{}-{}.{}".format(universitySeat, strToday, fileType)
    return excel.make_response(sheet, fileType, file_name=fileName)
    # DONDE DICE FILENAME PONER CSV


@checkUserAccess(rol='Programador UC', login_url='/error403/')
def publishOGSReport(request, universitySeatId):
    universitySeat = UniversitySeat.objects.get(pk=int(universitySeatId))
    if universitySeat.isOfficialDistributionOGSPublished:
        universitySeat.isOfficialDistributionOGSPublished = False
        message = f'Reporte de Distribución Oficial OGS de la sede {universitySeat.name} despublicado satisfactoriamente'
    else:
        universitySeat.isOfficialDistributionOGSPublished = True
        message = f'Reporte de Distribución Oficial de la sede OGS {universitySeat.name} generado y publicado satisfactoriamente'
    universitySeat.save()
    messages.success(request, message)
    return redirect('officialDistributionOGS')
