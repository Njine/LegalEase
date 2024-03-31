from django.urls import path
from . import views

urlpatterns = [
    path('error-list/', views.error_list, name='error_list'),
]
