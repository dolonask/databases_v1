from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.append_case, name='migrant_case'),
    path('cases/', views.cases, name='migrants_list'),
    path('update/<int:pk>', views.update_case, name="migrant_case_update"),
    path('delete/<int:pk>', views.delete_case, name="migrant_case_delete"),
    path('add-comment/<int:pk>', views.add_comment, name="migrant_case_add_comment"),
    path('show-comments/<int:pk>', views.show_comments, name="migrant_case_show_comments"),
    path('delete-comments/<int:pk>', views.delete_comment, name="migrant_case_delete_comment"),
    path('download-pdf/<int:pk>', views.case_download_pdf_view, name="migrant_case_download_pdf"),
    path('get-pdf/<int:pk>', views.case_render_pdf_view, name="migrant_case_get_pdf"),
    path('dict/regions', views.load_regions, name='migrant_regions_list'),
    path('test/<int:pk>', views.test, name='test'),
    path('data/', views.DataAPIView.as_view(), name='migrant_data'),
    path('data/get/', views.DataFilterAPI.as_view(), name='migrant_data_get'),
    path('case_files_download/<int:pk>/', views.case_files_download, name='migrant_case_files_download'),
    path('word/<int:pk>/', views.generate_case_word, name='migrant_case_word')
]