from django.conf.urls import url
from api.viewsPack.panelViews.students import typeOfStudentsView as views

urlpatterns = [
    url(r'^panel/typeOfStudents/$', views.allTypeOfStudents, name='allTypeOfStudents'),
    url(r'^panel/typeOfStudents/add/$', views.addTypeOfStudent, name='addTypeOfStudent'),
    url(r'^panel/typeOfStudents/delete/(?P<pk>\d+)/$', views.deleteTypeOfStudent, name='deleteTypeOfStudent'),
    url(r'^panel/typeOfStudents/edit/(?P<pk>\d+)/$', views.editTypeOfStudent, name='editTypeOfStudent'),
]
