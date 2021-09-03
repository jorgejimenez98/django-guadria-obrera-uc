from django.conf.urls import url
from api.viewsPack.panelViews.guards import dutyShiftsView as views

urlpatterns = [
    url(r'^panel/dutyShifts/$', views.dutyShiftsView, name='dutyShiftsView'),
    url(r'^panel/dutyShifts/add/$', views.addDutyShift, name='addDutyShift'),
    url(r'^panel/dutyShifts/delete/(?P<pk>\d+)/$', views.deleteDutyShift, name='deleteDutyShift'),
    url(r'^panel/dutyShifts/edit/(?P<pk>\d+)/$', views.editDutyShift, name='editDutyShift'),
]
