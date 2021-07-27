from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_case, name='strike_case'),
    path('cases/', views.cases, name='strikes_list'),
    path('update/<int:pk>', views.update_case, name="strike_case_update"),
    path('delete/<int:pk>', views.delete_case, name="strike_case_delete"),
    path('add-comment/<int:pk>', views.add_comment, name="strike_card_add_comment"),
    path('show-comments/<int:pk>', views.show_comments, name="strike_card_show_comments"),
    path('delete-comments/<int:pk>', views.delete_comment, name="strike_card_delete_comment"),
    path('dict/regions', views.load_regions, name='strike_regions_list'),
    path('download-pdf/<int:pk>', views.case_download_pdf_view, name="strike_case_download_pdf"),
    path('get-pdf/<int:pk>', views.case_render_pdf_view, name="strike_case_get_pdf"),
    path('data/', views.DataAPIView.as_view(), name="strike_data_api"),
    path('data/get/', views.DataFilterAPI.as_view(), name="strike_filter_data_api"),
    path('card_files_download/<int:pk>/', views.card_files_download, name='strike_card_files_download')
]