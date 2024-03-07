from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('register_user/', views.register_user, name='register_user'),
]
