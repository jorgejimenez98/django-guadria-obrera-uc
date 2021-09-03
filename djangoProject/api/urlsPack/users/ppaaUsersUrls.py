from django.conf.urls import url
from api.viewsPack.panelViews.users import ppaaUsersView as views

urlpatterns = [
    url(r'^panel/users/ppaa/$', views.ppaaUsersList, name='ppaaUsersList'),
    url(r'^panel/users/ppaa/add/$', views.addPPAAUser, name='addPPAAUser'),
    url(r'^panel/users/ppaa/delete/(?P<pk>\d+)/$', views.deletePPAAUser, name='deletePPAAUser'),
    url(r'^panel/users/ppaa/edit/(?P<pk>\d+)/$', views.editPPAAUser, name='editPPAAUser'),
    url(r'^panel/users/ppaa/changeRol/(?P<pk>\d+)/$', views.changePPAAUserRol, name='changePPAAUserRol'),
]
