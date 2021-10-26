from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='analytic_home'),
    path('migrant/', views.migrant_analytic, name='migrant_analytic'),
    path('strike/', views.strike_analytic, name='strike_analytic'),
    path('work/', views.work_analytic, name='work_analytic'),
    path('migrant/search/', views.MigrantResultApiView.as_view()),
    path('work/search/', views.WorkResultApiView.as_view(), name="modal_search"),
    path('strike/search/', views.StrikeResultApiView.as_view()),
]