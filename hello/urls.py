from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout,login


urlpatterns=[
    url(r'^$',views.home),
    url(r'^login/$',views.log,name='log'),
    url(r'^logout/$',logout,{'template_name':'hello/logout.html'}),
    url(r'^register/$', views.register ,name='register'),
    url(r'^profile/$', views.view_profile ,name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile ,name='edit_profile'),
]
