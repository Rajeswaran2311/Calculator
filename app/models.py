from django.db import models

# Create your models here.
class Todo_entry(models.Model):
    entry=models.CharField(max_length=100)