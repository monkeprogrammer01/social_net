from django.db import models
from users.models import User
from django.utils import timezone


class Chat(models.Model):
    user1 = models.ForeignKey(User, related_name="chat_user1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name="chat_user2", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user1', 'user2')


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=str(timezone.now))

