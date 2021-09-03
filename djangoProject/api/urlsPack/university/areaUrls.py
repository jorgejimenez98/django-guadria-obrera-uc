from django.conf.urls import url
from api.viewsPack.panelViews.univesity import areaView as views

urlpatterns = [
    url(r'^panel/areas/$', views.areasList, name='areasList'),
    url(r'^panel/areas/add/$', views.addArea, name='addArea'),
    url(r'^panel/areas/delete/(?P<pk>\d+)/$', views.deleteArea, name='deleteArea'),
    url(r'^panel/areas/edit/(?P<pk>\d+)/$', views.editArea, name='editArea'),
]
