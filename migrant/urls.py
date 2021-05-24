from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.append_case, name='migrant_case'),
    path('cases/', views.cases, name='migrants_list'),
]