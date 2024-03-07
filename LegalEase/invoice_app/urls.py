from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns for invoice_app views
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/generate/', views.invoice_generate, name='invoice_generate'),
    path('invoices/<int:invoice_id>/update/', views.invoice_update, name='invoice_update'),
    path('invoices/<int:invoice_id>/delete/', views.invoice_delete, name='invoice_delete'),
]
