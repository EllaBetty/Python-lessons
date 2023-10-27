from django.db import models
from django.utils.text import Truncator

# Create your models here.

from django.contrib.auth.models import User
from django.utils.html import mark_safe # Sep22nd
from markdown import markdown #  Sep22nd

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()
    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.DO_NOTHING)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.DO_NOTHING)
    views = models.PositiveIntegerField(default=0)  # <- here WE ADD A NEW PROPERTY Aug 4th
    def __str__(self):
        return self.subject
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.DO_NOTHING)
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
    def get_message_as_markdown(self): # Sep 22nd
        return mark_safe(markdown(self.message, safe_mode='escape'))
