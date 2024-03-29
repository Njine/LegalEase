from django.shortcuts import render, redirect, get_object_or_404
from .models import Case
from .forms import CaseForm

def case_list(request):
    cases = Case.objects.all()
    return render(request, 'case_app/case_list.html', {'cases': cases})

def case_detail(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    return render(request, 'case_app/case_detail.html', {'case': case})

def create_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm()
    return render(request, 'case_app/create_case.html', {'form': form})

def update_case(request, case_id):
    case = get_object_or_404(Case, pk=case_id)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case_detail', case_id=case_id)
    else:
        form = CaseForm(instance=case)
    return render(request, 'case_app/update_case.html', {'form': form, 'case': case})
