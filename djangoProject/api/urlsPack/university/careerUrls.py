from django.conf.urls import url
from api.viewsPack.panelViews.univesity import careersView as views

urlpatterns = [
    url(r'^panel/careers/$', views.careersList, name='careersList'),
    url(r'^panel/careers/add/$', views.addCareer, name='addCareer'),
    url(r'^panel/careers/delete/(?P<pk>\d+)/$', views.deleteCareer, name='deleteCareer'),
    url(r'^panel/careers/edit/(?P<pk>\d+)/$', views.editCareer, name='editCareer'),
]
