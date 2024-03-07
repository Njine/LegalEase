from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('create_client/', views.create_client, name='create_client'),
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
]
