from django.urls import path
from . import views


#url config

urlpatterns = [
    path('', views.hello, name='hello')
]
