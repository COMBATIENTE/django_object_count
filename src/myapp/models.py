from django.db import models

# Create your models here.

class PageView(models.Model):
    hits=models.IntegerField(default=0)