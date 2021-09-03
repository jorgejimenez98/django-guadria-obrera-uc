from django.conf.urls import url
from api.viewsPack.panelViews.users import deansView as views

urlpatterns = [
    url(r'^panel/users/dean/$', views.deanUsersList, name='deanUsersList'),
    url(r'^panel/users/dean/add/$', views.addDeanUser, name='addDeanUser'),
    url(r'^panel/users/dean/delete/(?P<pk>\d+)/$', views.deleteDeanUser, name='deleteDeanUser'),
    url(r'^panel/users/dean/edit/(?P<pk>\d+)/$', views.editDeanUser, name='editDeanUser'),
    url(r'^panel/users/dean/changeRol/(?P<pk>\d+)/$', views.changeDeanUserRol, name='changeDeanUserRol'),
]
