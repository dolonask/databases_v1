from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.append_case, name='migrant_case'),
    path('cases/', views.cases, name='migrants_list'),
    path('update/<int:pk>', views.update_case, name="migrant_case_update"),
    path('delete/<int:pk>', views.delete_case, name="migrant_case_delete"),
    path('download/<int:case_id>', views.download, name="migrant_files_download"),

    path('dict/regions', views.load_regions, name='migrant_regions_list'),
]