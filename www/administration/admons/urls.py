from django.urls import path

from admons.views import util

app_name = 'admons'


urlpatterns = [
    path('', util.health, name='health')
]