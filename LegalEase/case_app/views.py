from document_app.models import Document
from django.shortcuts import render, redirect, get_object_or_404
from .models import Case

def case_list(request):
    cases = Case.objects.all()
    return render(request, 'case_app/case_list.html', {'cases': cases})

def case_detail(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    return render(request, 'case_app/case_detail.html', {'case': case})

def create_case(request):
    if request.method == 'POST':
        # Process the form data and create a new case
        # ...
        return redirect('case_list')  # Redirect to the case list page after creating the case
    else:
        # Render the form to create a new case
        return render(request, 'case_app/create_case.html')

def update_case(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        # Process the form data and update the existing case
        # ...
        return redirect('case_detail', case_id=case_id)  # Redirect to the case detail page after updating the case
    else:
        # Render the form to update the existing case
        return render(request, 'case_app/update_case.html', {'case': case})
