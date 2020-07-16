from django.db import models

# Create your models here.
class email(models.Model):
    mail=models.CharField(max_length=100)