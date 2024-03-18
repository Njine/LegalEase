from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('generate/', views.invoice_generate, name='invoice_generate'),
    path('<int:invoice_id>/update/', views.invoice_update, name='invoice_update'),
    path('<int:invoice_id>/delete/', views.invoice_delete, name='invoice_delete'),
]