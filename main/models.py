from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Theme(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, default="white")
    font = models.CharField(max_length=50, default="Arial")

