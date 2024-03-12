from django.contrib import admin
from .models import Case, CourtLevel
from document_app.models import Document  # Import Document model from the correct module

admin.site.register(Case)
admin.site.register(CourtLevel)
admin.site.register(Document)  # Register Document model
