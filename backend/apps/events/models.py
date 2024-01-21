from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    organizer = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='created_events',
        null=True
    )
    participants = models.ManyToManyField(
        User,
        related_name='events',
    )
