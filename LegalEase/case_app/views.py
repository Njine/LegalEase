from django.shortcuts import render
from .models import Case
from django.shortcuts import render, get_object_or_404
from .models import Case

def case_list(request):
    cases = Case.objects.all()
    return render(request, 'case_app/case_list.html', {'cases': cases})

def case_detail(request, case_id):
    case = Case.objects.get(pk=case_id)
    return render(request, 'case_app/case_detail.html', {'case': case})

def create_case(request):
        if request.method == 'POST':
            # Process the form data and create a new case
            # ...
            return redirect('case_list')  # Redirect to the case list page after creating the case
        else:
            # Render the form to create a new case
            return render(request, 'case_app/create_case.html')