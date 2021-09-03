from django.conf.urls import url
from api.viewsPack.panelViews.users import programmerFacultyViews as views

urlpatterns = [
    url(r'^panel/users/programmerFaculty/$', views.programmerFacultyUsersList, name='programmerFacultyUsersList'),
    url(r'^panel/users/programmerFaculty/add/$', views.addProgrammerFacultyUser, name='addProgrammerFacultyUser'),
    url(r'^panel/users/programmerFaculty/delete/(?P<pk>\d+)/$', views.deleteProgrammerFacultyUser, name='deleteProgrammerFacultyUser'),
    url(r'^panel/users/programmerFaculty/edit/(?P<pk>\d+)/$', views.editProgrammerFacultyUser, name='editProgrammerFacultyUser'),
    url(r'^panel/users/programmerFaculty/changeRol/(?P<pk>\d+)/$', views.changeProgrammerFacultyUserRol, name='changeProgrammerFacultyUserRol'),
]
