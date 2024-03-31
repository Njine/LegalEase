from django.urls import path
from . import views

urlpatterns = [
    path('user-profiles/', views.user_list, name='user_profile_list'),
    path('user-profiles/<int:user_id>/', views.user_detail, name='user_profile_detail'),
]
