from django.shortcuts import render, get_object_or_404
from .models import Case

def case_list(request):
    """View function for listing cases."""
    cases = Case.objects.all()
    return render(request, 'case_app/case_list.html', {'cases': cases})

def case_detail(request, case_id):
    """View function for displaying case details."""
    case = get_object_or_404(Case, pk=case_id)
    return render(request, 'case_app/case_detail.html', {'case': case})
