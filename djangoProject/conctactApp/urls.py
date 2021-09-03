from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contact/$', views.contactView, name='contactView'),
    url(r'^contact/add/$', views.addNewContactMessage, name='addNewContactMessage'),
]
