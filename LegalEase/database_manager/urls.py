from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns for database_manager views
    path('connect/', views.connect_to_database, name='database_connect'),
    path('insert/', views.database_insert, name='database_insert'),
    path('query/', views.query_database, name='database_query'),
]
