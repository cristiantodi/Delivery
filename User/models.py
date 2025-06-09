from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Cargo(models.Model):
    nombre  = models.CharField(blank=True , default="N/A" , null=True, max_length=100)
    
    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    cargo       = models.ManyToManyField(Cargo)
    telefono    = models.CharField(max_length=20, blank=True, null=True)
    local       = models.CharField(blank=True , default="N/A" , null=True, max_length=100)
    

    def __str__(self):
        return self.username