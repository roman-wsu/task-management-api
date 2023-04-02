from django.db import models
import uuid
from apps.users.models import User


class Column(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='columns')
    title = models.CharField(max_length=256)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    text = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')
    date_created = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='date updated', auto_now=True)
