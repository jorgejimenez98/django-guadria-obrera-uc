from django.conf.urls import url
from api.viewsPack.panelViews.univesity import departmentView as views

urlpatterns = [
    url(r'^panel/departments/$', views.departmentsList, name='departmentsList'),
    url(r'^panel/departments/add/$', views.addDepartment, name='addDepartment'),
    url(r'^panel/departments/delete/(?P<pk>\d+)/$', views.deleteDepartment, name='deleteDepartment'),
    url(r'^panel/departments/edit/(?P<pk>\d+)/$', views.editDepartment, name='editDepartment'),
]
