from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_error, name='log_error'),
    path('log-error/', views.log_error, name='log_error_direct'),
]