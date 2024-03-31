from django.shortcuts import render, redirect, get_object_or_404
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_app/client_list.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_app/client_detail.html', {'client': client})

def create_client(request):
    if request.method == 'POST':
        # Process the form data and create a new client
        client = Client(name=request.POST['name'], contact_information=request.POST['contact_information'])
        client.save()
        return redirect('client_list')
    else:
        return render(request, 'client_app/create_client.html')

def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        # Process the form data and update the client
        client.name = request.POST['name']
        client.contact_information = request.POST['contact_information']
        client.save()
        return redirect('client_detail', client_id=client_id)
    else:
        return render(request, 'client_app/update_client.html', {'client': client})

def delete_client(client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect('client_list')  # Redirect to the client list view after deleting the client
# Path: LegalEase/client_app/templates/client_app/client_list.html
# Compare this snippet from LegalEase/authentication_manager/templates/authentication_manager/login.html:
