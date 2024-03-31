from django.shortcuts import render
from .models import ErrorLogger

def error_list(request):
    errors = ErrorLogger.objects.all()
    return render(request, 'error_logger/error_list.html', {'errors': errors})
