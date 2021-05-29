from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.append_case, name='migrant_case'),
    path('cases/', views.cases, name='migrants_list'),
    path('update/<str:pk>', views.update_case, name="migrant_case_update"),
    path('download/<str:case_id>', views.download, name="migrant_files_download"),

]