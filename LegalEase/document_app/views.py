from django.shortcuts import render, get_object_or_404
from .models import Document
from .forms import DocumentForm

def document_list(request):
    """View function for listing documents."""
    documents = Document.objects.all()
    return render(request, 'document_app/document_list.html', {'documents': documents})

def document_detail(request, document_id):
    """View function for displaying document details."""
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'document_app/document_detail.html', {'document': document})

def document_upload(request):
    """View function for uploading a new document."""
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document_app/document_upload.html', {'form': form})

def document_update(request, document_id):
    """View function for updating an existing document."""
    document = get_object_or_404(Document, pk=document_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'document_app/document_update.html', {'form': form})

def document_delete(request, document_id):
    """View function for deleting an existing document."""
    document = get_object_or_404(Document, pk=document_id)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'document_app/document_delete.html', {'document': document})
