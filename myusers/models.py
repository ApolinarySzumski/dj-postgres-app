from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    connections = models.IntegerField(max_length=int)