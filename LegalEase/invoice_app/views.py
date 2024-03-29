from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice
from .forms import InvoiceForm

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_app/invoice_list.html', {'invoices': invoices})

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    return render(request, 'invoice_app/invoice_detail.html', {'invoice': invoice})

def invoice_form(request, invoice_id=None):
    if invoice_id:
        invoice = get_object_or_404(Invoice, pk=invoice_id)
    else:
        invoice = None

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'invoice_app/invoice_form.html', {'form': form})

def invoice_delete(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'invoice_app/invoice_confirm_delete.html', {'invoice': invoice})
