from django.shortcuts import render, get_object_or_404
from .models import Document

def document_list(request):
    """View function for listing documents."""
    documents = Document.objects.all()
    return render(request, 'document_app/document_list.html', {'documents': documents})

def document_detail(request, document_id):
    """View function for displaying document details."""
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'document_app/document_detail.html', {'document': document})
