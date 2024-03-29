# Import necessary modules
from django.contrib import admin
from .models import CourtType, Court, CourtLevel, Case
# Register the models with the admin site
admin.site.register(CourtType)
admin.site.register(Court)
admin.site.register(CourtLevel)
admin.site.register(Case)
