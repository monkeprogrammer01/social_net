from django.urls import path
from messenger.views import send_message, create_chat, chat_combined

app_name = 'messenger'

urlpatterns = [
    path('', chat_combined, name="chat_combined"),
    path('chat/<int:chat_id>/', chat_combined, name="chat_combined"),
    path('chat/<int:chat_id>/send_message/', send_message, name="send_message"),
    path('create_chat/<int:user_id>/', create_chat, name='create_chat'),
]