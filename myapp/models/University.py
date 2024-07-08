from django.db import models
from django.contrib.auth.models import User

class University(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=50)
    web_page = models.URLField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, related_name='universities_created', on_delete=models.SET_NULL, null=True, blank=True)
    user_modified = models.ForeignKey(User, related_name='universities_modified', on_delete=models.SET_NULL, null=True, blank=True)


    
# Arce Mayhua Leonardo Ruben    