from django.conf.urls import url
from api.viewsPack.panelViews.users import headDepartmentsView as views

urlpatterns = [
    url(r'^panel/users/headDepartments/$', views.headDepartmentsUsersList, name='headDepartmentsUsersList'),
    url(r'^panel/users/headDepartments/add/$', views.addHeadDepartmentUser, name='addHeadDepartmentUser'),
    url(r'^panel/users/headDepartments/delete/(?P<pk>\d+)/$', views.deleteHeadDepartmentUser, name='deleteHeadDepartmentUser'),
    url(r'^panel/users/headDepartments/edit/(?P<pk>\d+)/$', views.editHeadDepartmentUser, name='editHeadDepartmentUser'),
    url(r'^panel/users/headDepartments/changeRol/(?P<pk>\d+)/$', views.changeHeadDepartmentUserRol, name='changeHeadDepartmentUserRol'),
]