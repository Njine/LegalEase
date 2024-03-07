from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns for document_app views
    path('documents/', views.document_list, name='document_list'),
    path('documents/<int:document_id>/', views.document_detail, name='document_detail'),
    path('documents/upload/', views.document_upload, name='document_upload'),
    path('documents/<int:document_id>/update/', views.document_update, name='document_update'),
    path('documents/<int:document_id>/delete/', views.document_delete, name='document_delete'),
]
