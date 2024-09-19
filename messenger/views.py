from django.shortcuts import render, redirect, get_object_or_404
from messenger.models import Chat, Message
from users.models import User
from django.db.models import Q


def chat_combined(request, chat_id=None):
    chats = Chat.objects.filter(Q(user1=request.user) | Q(user2=request.user))
    users = request.user.friends.all()
    selected_chat = None
    messages = []

    if chat_id:
        selected_chat = get_object_or_404(Chat, id=chat_id)
        messages = Message.objects.filter(chat=selected_chat)

    context = {
        'chats': chats,
        'selected_chat': selected_chat,
        'messages': messages,
        'users': users,


    }
    return render(request, 'messenger/chats.html', context)


def send_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(chat=chat, sender=request.user, content=content)
    return redirect('messenger:chat_combined', chat_id=chat_id)


def create_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    if request.user.id < other_user.id:
        user1 = request.user
        user2 = other_user
    else:
        user1 = other_user
        user2 = request.user

    chat, created = Chat.objects.get_or_create(user1=user1, user2=user2)
    return redirect('messenger:chat_combined', chat_id=chat.id)
