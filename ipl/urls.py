from django.urls import path, include
from django.conf.urls import url

from . import views


urlpatterns = [
    url('home', views.home, name='home'),
    url('input', views.input, name='input'),
    url('output', views.output, name='output'),
    url('alternatives', views.alternatives, name='alternatives'),
    url('predict', views.predict, name='predict'),
    url('options', views.options, name='options'),
    url('charts', views.charts, name='charts')
]
