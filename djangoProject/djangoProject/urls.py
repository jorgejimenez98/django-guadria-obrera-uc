from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from api.views import error404NotFoundView

urlpatterns = [
    path('admin/', admin.site.urls),
    # PUBLIC URLS
    path('', include('api.urls')),
    path('', include('conctactApp.urls')),
    # PANEL URLS
    path('', include('api.urlsPack.studentsStuff.provinceUrls')),
    path('', include('api.urlsPack.studentsStuff.municipalitiesUrls')),
    path('', include('api.urlsPack.studentsStuff.typeOfStudentsUrls')),
    path('', include('api.urlsPack.studentsStuff.typeOfCoursesUrls')),
    path('', include('api.urlsPack.studentsStuff.sourceOfIncomeUrls')),
    path('', include('api.urlsPack.studentsStuff.stateUrls')),
    path('', include('api.urlsPack.studentsStuff.studentsUrls')),

    path('', include('api.urlsPack.university.facultyUrls')),
    path('', include('api.urlsPack.university.areaUrls')),
    path('', include('api.urlsPack.university.departmentsUrl')),
    path('', include('api.urlsPack.university.careerUrls')),
    path('', include('api.urlsPack.university.universitySeatUrls')),

    path('', include('api.urlsPack.users.usersUrls')),
    path('', include('api.urlsPack.users.ppaaUsersUrls')),
    path('', include('api.urlsPack.users.deansUrls')),
    path('', include('api.urlsPack.users.headDepartmentsUrls')),
    path('', include('api.urlsPack.users.programmerFacultyUrls')),

    path('', include('api.urlsPack.guards.officialDistributionOGSUrls')),
    path('', include('api.urlsPack.guards.officialDistributionAOGSUrls')),
    path('', include('api.urlsPack.guards.dutyShiftsUrls')),
    # 404 ERROR URL
    url(r'^.*/$', error404NotFoundView, name='error404NotFoundView'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
