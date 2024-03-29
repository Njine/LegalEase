from django.shortcuts import render
from .models import CollaborationBoard, ChatMessage

def collaboration_board(request):
    collaboration_boards = CollaborationBoard.objects.all()
    return render(request, 'collaboration_app/collaboration_board.html', {'collaboration_boards': collaboration_boards})

def collaboration_chat(request):
    chat_messages = ChatMessage.objects.all()
    return render(request, 'collaboration_app/collaboration_chat.html', {'chat_messages': chat_messages})
