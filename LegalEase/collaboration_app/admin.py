# Import necessary modules
from django.contrib import admin
from .models import CollaborationBoard, ChatMessage

# Register the models with the admin site
admin.site.register(CollaborationBoard)
admin.site.register(ChatMessage)
