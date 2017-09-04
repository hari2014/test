
from django.conf.urls import url,include
from django.contrib import admin
from dash import views

urlpatterns = [
    url(r'^$',views.login_redirect,name='login_redirect'),
    url(r'^hello/', include('hello.urls')),
    url(r'^admin/', admin.site.urls),
]
