from django.conf.urls import url
from api.viewsPack.panelViews.students import sourceOfIncomeViews as views

urlpatterns = [
    url(r'^panel/sourceOfIncomes/$', views.allSourceIncomes, name='allSourceIncomes'),
    url(r'^panel/sourceOfIncomes/add/$', views.addSourceOfIncome, name='addSourceOfIncome'),
    url(r'^panel/sourceOfIncomes/delete/(?P<pk>\d+)/$', views.deleteSourceOfIncome, name='deleteSourceOfIncome'),
    url(r'^panel/sourceOfIncomes/edit/(?P<pk>\d+)/$', views.editSourceOfIncome, name='editSourceOfIncome'),
]
