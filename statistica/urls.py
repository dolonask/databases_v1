from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='analytic_home'),
    path('migrant/', views.migrant_analityc, name='migrant_analytic'),
]