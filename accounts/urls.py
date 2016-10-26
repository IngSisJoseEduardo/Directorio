from django.conf.urls import url
from accounts.views import login_view, register_view, logout_view, word

urlpatterns = [
    url(r'^$',login_view, name = 'login'),
    url(r'^registrar/$',register_view,name = 'register'),
    url(r'^salir/$',logout_view, name = 'logout'),
    url(r'^prueba/$', word),
]
