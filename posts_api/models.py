from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=256)
    time_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.body[0:50]

    class Meta:
        ordering = ['-time_created']