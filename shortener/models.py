from django.db import models

class Url(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  expanded = models.CharField(max_length=256)
  shortened = models.CharField(max_length=256)  