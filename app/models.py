from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True, default='')
    def __str__(self):
        return self.title

