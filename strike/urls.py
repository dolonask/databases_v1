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
]