from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.append_case, name='strike_case'),
    path('cases/', views.cases, name='strikes_list'),
]