from django.shortcuts import render
from .models import Case

def case_list(request):
    cases = Case.objects.all()
    return render(request, 'case_app/case_list.html', {'cases': cases})

def case_detail(request, case_id):
    case = Case.objects.get(pk=case_id)
    return render(request, 'case_app/case_detail.html', {'case': case})
