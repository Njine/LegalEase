from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def log_error(request):
    """View function for logging errors."""
    if request.method == 'POST':
        # Retrieve error details from the request
        error_message = request.POST.get('error_message')
        error_code = request.POST.get('error_code')
        # Log the error to a file or database
        # Example: error_logger.log_error(error_message, error_code)
        # Replace 'error_logger.log_error' with your actual function for logging errors
        return render(request, 'error_logger/success.html')
    return render(request, 'error_logger/log_error.html')
