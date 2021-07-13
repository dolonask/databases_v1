from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_case, name='work_case'),
    path('cases/', views.cases, name='works_list'),
    path('update/<int:pk>/', views.update_case, name="work_case_update"),
    path('delete/<int:pk>/', views.delete_case, name="work_case_delete"),
    path('add-comment/<int:pk>/', views.add_comment, name="work_case_add_comment"),
    path('download-pdf/<int:pk>/', views.case_download_pdf_view, name="work_case_download_pdf"),
    path('get-pdf/<int:pk>/', views.case_render_pdf_view, name="work_case_get_pdf"),
    path('show-comments/<int:pk>/', views.show_comments, name="work_case_show_comments"),
    path('delete-comments/<int:pk>/', views.delete_comment, name="work_case_delete_comment"),
    path('dict/regions/', views.load_regions, name='works_regions_list'),
    path('data/', views.DataAPIView.as_view(), name='data'),
    path('data/get/', views.DataFilterAPI.as_view(), name='data_get')
]