from django.conf.urls import url
from api.viewsPack.panelViews.students import provinceVIews as views

urlpatterns = [
    url(r'^panel/provinces/$', views.provinceView, name='provinceView'),
    url(r'^panel/provinces/add/$', views.addProvince, name='addProvince'),
    url(r'^panel/provinces/delete/(?P<pk>\d+)/$', views.deleteProvince, name='deleteProvince'),
    url(r'^panel/provinces/edit/(?P<pk>\d+)/$', views.editProvince, name='editProvince'),
]
