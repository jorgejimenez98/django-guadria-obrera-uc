from django.conf.urls import url
from api.viewsPack.panelViews.guards import officialDistributionAOGSView as views

urlpatterns = [
    url(r'^panel/officialDistribution/AOGS/$', views.officialDistributionAOGS, name='officialDistributionAOGS'),
    # url(r'^panel/officialDistributionOGS/(?P<universitySeat>.*)/$', views.officialOGSDistributionBySeatName, name='officialOGSDistributionBySeatName'),
    # url(r'^panel/officialDistribution/OGS/edit/(?P<universitySeat>.*)/(?P<day>\d+)/$', views.editOfficialOGSDistributionBySeatAndDayOfMonth, name='editOfficialOGSDistributionBySeatAndDayOfMonth'),
    # url(r'^panel/officialDistribution/OGS/exportToExcel/(?P<universitySeat>.*)/(?P<fileType>.*)/$', views.exportToExcel, name='exportToExcel'),
]
