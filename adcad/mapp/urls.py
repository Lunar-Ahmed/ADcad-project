from django.urls import path
from . import views


urlpatterns = [
    path('group/', views.group, name='group'),
    path('group/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
        path('testing/', views.testing, name='testing'),  
]
