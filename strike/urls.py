from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.append_case, name='strike_case'),
    path('list/', views.StrikeListView.as_view(), name='strikes_list')
]