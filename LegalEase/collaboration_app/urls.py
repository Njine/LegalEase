from django.urls import path
from . import views

urlpatterns = [
    path('collaboration/board/', views.collaboration_board, name='collaboration_board'),
    path('collaboration/chat/', views.collaboration_chat, name='collaboration_chat'),
]
