from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_app/contact_list.html', {'contacts': contacts})

def contact_detail(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact_app/contact_detail.html', {'contact': contact})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_app/create_contact.html', {'form': form})

def edit_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_app/edit_contact.html', {'form': form})

def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_app/delete_contact.html', {'contact': contact})
