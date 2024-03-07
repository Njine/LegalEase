from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_error, name='log_error'),
]
