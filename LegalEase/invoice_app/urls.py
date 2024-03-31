from django.urls import path
from . import views

urlpatterns = [
    path('invoice-list/', views.invoice_list, name='invoice_list'),
    path('invoice-detail/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('invoice-form/', views.invoice_form, name='invoice_form'),
    path('invoice-form/<int:invoice_id>/', views.invoice_form, name='invoice_form_update'),
    path('invoice-delete/<int:invoice_id>/', views.invoice_delete, name='invoice_delete'),
]
