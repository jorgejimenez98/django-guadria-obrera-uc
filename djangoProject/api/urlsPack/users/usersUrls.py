from django.conf.urls import url
from api.viewsPack.panelViews.users import usersView as views

urlpatterns = [
    url(r'^panel/users/$', views.usersList, name='usersList'),
    url(r'^panel/users/add/$', views.addUser, name='addUser'),
    url(r'^panel/users/delete/(?P<pk>\d+)/$', views.deleteUser, name='deleteUser'),
    url(r'^panel/users/edit/(?P<pk>\d+)/$', views.editUser, name='editUser'),
    url(r'^panel/users/changePassword/(?P<pk>\d+)/$', views.changeUserPassword, name='changeUserPassword'),
]
