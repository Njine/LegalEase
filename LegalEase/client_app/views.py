from django.shortcuts import render
from .models import Client
from django.shortcuts import render, redirect
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_app/client_list.html', {'clients': clients})


def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'client_app/client_detail.html', {'client': client})

def create_client(request):
    if request.method == 'POST':
        # Process the form data and create a new client
        # Example: client = Client(name=request.POST['name'], ...)
        # client.save()
        return redirect('client_list')
    else:
        return render(request, 'client_app/create_client.html')

def update_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    if request.method == 'POST':
        # Process the form data and update the client
        # Example: client.name = request.POST['name']
        # client.save()
        return redirect('client_detail', client_id=client_id)
    else:
        return render(request, 'client_app/update_client.html', {'client': client})