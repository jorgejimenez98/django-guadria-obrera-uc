from django.conf.urls import url
from api.viewsPack.panelViews.univesity import facultyViews as views

urlpatterns = [
    url(r'^panel/faculty/$', views.facultyList, name='facultyList'),
    url(r'^panel/faculty/add/$', views.addFaculty, name='addFaculty'),
    url(r'^panel/faculty/delete/(?P<pk>\d+)/$', views.deleteFaculty, name='deleteFaculty'),
    url(r'^panel/faculty/edit/(?P<pk>\d+)/$', views.editFaculty, name='editFaculty'),
]
