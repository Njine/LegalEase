from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/<int:contact_id>/', views.contact_detail, name='contact_detail'),
    path('contacts/create/', views.create_contact, name='create_contact'),
    path('contacts/<int:contact_id>/update/', views.edit_contact, name='update_contact'),
    path('contacts/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]
