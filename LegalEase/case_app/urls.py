from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list, name='case_list'),
    path('case/<int:case_id>/', views.case_detail, name='case_detail'),
    path('create_case/', views.create_case, name='create_case'),
    path('update_case/<int:case_id>/', views.update_case, name='update_case'),
]
