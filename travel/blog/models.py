from django.db import models

class Contact(models.Model):
  name = models.CharField(blank=False, max_length=50)
  email = models.EmailField(blank=False, max_length=50)
  subject = models.TextField(blank=False)
  message = models.TextField(blank=False)