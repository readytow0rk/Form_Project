# models.py
from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=4)
    short = models.CharField(max_length=4)
