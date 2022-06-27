from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE,)
    created_date = models.DateTimeField() 
    active = models.BooleanField(default=True)