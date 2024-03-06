from django.contrib import admin
from .models import Case, CourtLevel, Document

# Register the Case, CourtLevel, and Document models with the admin interface
admin.site.register(Case)
admin.site.register(CourtLevel)
admin.site.register(Document)
