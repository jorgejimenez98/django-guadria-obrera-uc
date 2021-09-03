from django.conf.urls import url
from api.viewsPack.panelViews.students import studentsViews as views

urlpatterns = [
    url(r'^panel/students/$', views.studentsList, name='studentsList'),
    # url(r'^panel/states/add/$', views.addState, name='addState'),
    # url(r'^panel/states/delete/(?P<pk>\d+)/$', views.deleteState, name='deleteState'),
    # url(r'^panel/states/edit/(?P<pk>\d+)/$', views.editState, name='editState'),
]
