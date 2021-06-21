from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_case, name='work_case'),
    path('cases/', views.cases, name='works_list'),
    path('update/<int:pk>', views.update_case, name="work_case_update"),
    path('delete/<int:pk>', views.delete_case, name="work_case_delete"),
    path('add-comment/<int:pk>', views.add_comment, name="work_case_add_comment"),
    path('show-comments/<int:pk>', views.show_comments, name="work_case_show_comments"),
    path('delete-comments/<int:pk>', views.delete_comment, name="work_case_delete_comment"),
    path('dict/regions', views.load_regions, name='works_regions_list'),
]