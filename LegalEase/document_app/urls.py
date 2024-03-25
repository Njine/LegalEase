from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    # Define URL patterns for document_app views
    path('', views.document_list, name='document_list'),
    path('<int:document_id>/', views.document_detail, name='document_detail'),
    path('upload/', views.document_upload, name='document_upload'),
    path('<int:document_id>/update/', views.document_update, name='document_update'),
    path('<int:document_id>/delete/', views.document_delete, name='document_delete'),
]