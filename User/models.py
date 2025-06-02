from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Cargo(models.Model):
    nombre  = models.CharField(blank=True , default="N/A" , null=True, max_length=50)
    
    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    cargo   = models.ManyToManyField(Cargo)
    local   = models.CharField(blank=True , default="N/A" , null=True, max_length=100)

    def __str__(self):
        return self.username