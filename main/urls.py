from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Z8XxfX6A92QrcZ6GSUtDJNgkn', views.create_super_user)
]