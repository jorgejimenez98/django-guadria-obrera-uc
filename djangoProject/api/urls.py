from django.conf.urls import url
from .viewsPack.publicViews import guardByUniversitySeatView as gView
from .viewsPack import authView as lView
from . import views

urlpatterns = [
    # PUBLIC URLS
    url(r'^$', views.homeView, name='homeView'),
    url(r'^noGuards/$', views.noGuardsView, name='noGuardsView'),
    url(r'^guard/universitySeat/(?P<pk>\d+)/$', gView.guardByUniversitySeatView, name='guardByUniversitySeatView'),

    # AUTHENTICATION URLS
    url(r'^auth/login/$', lView.loginView, name='loginView'),
    url(r'^auth/logout/$', lView.logoutView, name='logoutView'),
    url(r'^auth/loginUserToSite/$', lView.loginUserToTheSite, name='loginUserToTheSite'),

    # ADMINISTRATION PANEL URLS
    url(r'^panel/$', views.administrationPanelView, name='administrationPanelView'),

    # 403 ERROR URL
    url(r'^error403/$', views.error403AccessDeniedError, name='error403AccessDeniedError')
]
