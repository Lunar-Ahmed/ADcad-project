from django.urls import path
from . import views


urlpattterns = [
    path('group', views.group, name='group'),
]

