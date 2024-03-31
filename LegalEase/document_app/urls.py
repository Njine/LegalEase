from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.document_list, name='document_list'),
    path('detail/<int:document_id>/', views.document_detail, name='document_detail'),
    path('upload/', views.document_upload, name='document_upload'),
    path('update/<int:document_id>/', views.document_update, name='document_update'),
    path('delete/<int:document_id>/', views.document_delete, name='document_delete'),
]
