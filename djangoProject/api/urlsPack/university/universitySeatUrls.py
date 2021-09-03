from django.conf.urls import url
from api.viewsPack.panelViews.univesity import universitySeatView as views

urlpatterns = [
    url(r'^panel/universitySeat/$', views.universitySeatList, name='universitySeatList'),
    url(r'^panel/universitySeat/add/$', views.addUniversitySeat, name='addUniversitySeat'),
    url(r'^panel/universitySeat/delete/(?P<pk>\d+)/$', views.deleteUniversitySeat, name='deleteUniversitySeat'),
    url(r'^panel/universitySeat/edit/(?P<pk>\d+)/$', views.editUniversitySeat, name='editUniversitySeat'),
]
