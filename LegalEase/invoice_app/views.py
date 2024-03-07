from django.shortcuts import render, redirect
from .models import Invoice

def generate_invoice(request):
    """View function for generating invoices."""
    if request.method == 'POST':
        # Process form data to generate invoice
        # Example: invoice = Invoice.objects.create(amount=request.POST['amount'], due_date=request.POST['due_date'])
        # Replace 'Invoice.objects.create' with your actual logic for creating an invoice
        return redirect('invoice_detail', invoice.id)
    return render(request, 'invoice_app/generate_invoice.html')

def view_invoice(request, invoice_id):
    """View function for viewing invoice details."""
    invoice = Invoice.objects.get(pk=invoice_id)
    return render(request, 'invoice_app/view_invoice.html', {'invoice': invoice})
