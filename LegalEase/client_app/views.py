from django.shortcuts import render, get_object_or_404
from .models import Client

def client_list(request):
    """View function for listing clients."""
    clients = Client.objects.all()
    return render(request, 'client_app/client_list.html', {'clients': clients})

def client_detail(request, client_id):
    """View function for displaying client details."""
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_app/client_detail.html', {'client': client})
