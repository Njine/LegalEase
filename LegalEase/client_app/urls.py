from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/create/', views.create_client, name='create_client'),
    path('client/update/<int:client_id>/', views.update_client, name='update_client'),
    path('client/delete/<int:client_id>/', views.delete_client, name='delete_client'),
]
