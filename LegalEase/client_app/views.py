from django.shortcuts import render
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_app/client_list.html', {'clients': clients})

def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'client_app/client_detail.html', {'client': client})
