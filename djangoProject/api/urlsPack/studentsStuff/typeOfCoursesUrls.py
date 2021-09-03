from django.conf.urls import url
from api.viewsPack.panelViews.students import typeOfCoursesViews as views

urlpatterns = [
    url(r'^panel/typeOfCourses/$', views.allTypeOfCourses, name='allTypeOfCourses'),
    url(r'^panel/typeOfCourses/add/$', views.addTypeOfCourse, name='addTypeOfCourse'),
    url(r'^panel/typeOfCourses/delete/(?P<pk>\d+)/$', views.deleteTypeOfCourse, name='deleteTypeOfCourse'),
    url(r'^panel/typeOfCourses/edit/(?P<pk>\d+)/$', views.editTypeOfCourse, name='editTypeOfCourse'),
]
