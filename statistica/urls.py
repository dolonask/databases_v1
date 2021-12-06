from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='analytic_home'),
    path('migrant/', views.migrant_analytic, name='migrant_analytic'),
    path('strike/', views.strike_analytic, name='strike_analytic'),
    path('work/', views.work_analytic, name='work_analytic'),

    path('migrant/search/', views.MigrantResultApiView.as_view(), name="migrant_search"),
    path('work/search/', views.WorkResultApiView.as_view(), name="work_search"),
    path('strike/search/', views.StrikeResultApiView.as_view(), name="strike_search"),

    path('detail/<int:pk>/', views.case_detail, name='detail_case'),
    path('strike-detail/<int:pk>/', views.card_strike_detail, name='detail_strike'),
    path('migrant-detail/<int:pk>/', views.case_migrant_detail, name='detail_migrant'),

]