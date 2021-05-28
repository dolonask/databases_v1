from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_case, name='work_case'),
    path('cases/', views.cases, name='works_list'),
]