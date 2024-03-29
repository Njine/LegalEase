"""
URL configuration for LegalEase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('user_app.urls')),
    path('cases/', include('case_app.urls')),  # Add this line to include case_app URLs
    path('clients/', include('client_app.urls')),  # Include client_app URLs
    path('error-logger/', include('error_logger.urls')),  # Add this line to include error_logger app URLs
    path('documents/', include('document_app.urls')),  # Add this line to include document_app URLs
    path('invoices/', include('invoice_app.urls')),  # Add this line to include invoice_app URLs
    path('authentication/', include('authentication_manager.urls')),  # Add this line to include authentication_manager URLs
]
