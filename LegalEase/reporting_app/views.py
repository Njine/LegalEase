from django.shortcuts import render
from django_report_builder.tasks import email_report
from .models import Report

def report_generation(request):
    # Typical reports needed in a law firm
    law_firm_reports = [
        'Case Summaries',
        'Client Billing Report',
        'Court Appearance Schedule',
        'Legal Research Reports',
        'Client Matter Status',
        'Staff Performance Report',
        # Add more reports as needed
    ]

    # Additional context data
    context = {
        'law_firm_reports': law_firm_reports,
        # Add more context data as needed
    }

    # Render the report generation template with the provided context
    return render(request, 'report_builder/report_list.html', context)
