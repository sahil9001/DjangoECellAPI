from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=256)
    venue = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=10)
    details = models.TextField()
    details_html = models.TextField(blank=True)
    cover_pic = models.ImageField(upload_to='static/uploads/events/cover',default='/static/defaults/ecell.png', null=True, blank=True)
    icon = models.ImageField(upload_to='static/uploads/events/icon',default='static/defaults/ecell.png')
    email = models.EmailField(null=True, blank=True)
    flag = models.BooleanField(default=False)
    year = models.IntegerField(default=2019)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)