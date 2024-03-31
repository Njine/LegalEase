from django.urls import path
from . import views

urlpatterns = [
    path('connect/', views.connect_to_database, name='connect_to_database'),
    path('query/', views.query_database, name='query_database'),
    path('insert/', views.database_insert, name='database_insert'),
]
