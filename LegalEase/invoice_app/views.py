from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_app/invoice_list.html', {'invoices': invoices})

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    return render(request, 'invoice_app/invoice_detail.html', {'invoice': invoice})

def invoice_generate(request):
    if request.method == 'POST':
        # Process form data to generate a new invoice
        invoice = Invoice.objects.create(amount=request.POST['amount'], due_date=request.POST['due_date'])
        return redirect('invoice_detail', invoice_id=invoice.id)
    return render(request, 'invoice_app/invoice_generate.html')

def invoice_update(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        # Process form data to update the invoice
        invoice.amount = request.POST['amount']
        invoice.due_date = request.POST['due_date']
        invoice.save()
        return redirect('invoice_detail', invoice_id=invoice_id)
    return render(request, 'invoice_app/invoice_update.html', {'invoice': invoice})

def invoice_delete(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        # Delete the invoice
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'invoice_app/invoice_confirm_delete.html', {'invoice': invoice})
