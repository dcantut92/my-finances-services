from django.urls import path

from account.views import util

app_name = 'account'


urlpatterns = [
    path('', util.health, name='health')
]