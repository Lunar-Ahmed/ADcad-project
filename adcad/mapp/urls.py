from django.urls import path
from . import views
# from .views import display_inputs_view

urlpatterns = [
    path('group/', views.group, name='group'),
    path('group/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),  
    path('table/', views.table_view, name='table_view'),
    
    # path('display-inputs/', display_inputs_view, name='display_inputs_view'),
]
