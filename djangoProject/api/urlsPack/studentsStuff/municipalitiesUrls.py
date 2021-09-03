from django.conf.urls import url
from api.viewsPack.panelViews.students import municipalitiesView as views

urlpatterns = [
    url(r'^panel/municipalities/$', views.municipalitiesView, name='municipalitiesView'),
    url(r'^panel/municipalities/add/$', views.addMunicipality, name='addMunicipality'),
    url(r'^panel/municipalities/delete/(?P<pk>\d+)/$', views.deleteMunicipality, name='deleteMunicipality'),
    url(r'^panel/municipalities/edit/(?P<pk>\d+)/$', views.editMunicipality, name='editMunicipality'),
]
