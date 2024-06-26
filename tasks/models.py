from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default="task1")
    
    def __str__(self):
        return self.body[0:50] #to get the first 50 chars
    
    