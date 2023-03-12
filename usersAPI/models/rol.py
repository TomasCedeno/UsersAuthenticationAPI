from django.db import models

from .permission import Permission

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Rol Name', max_length=30, unique=True)
    permissions = models.ManyToManyField(Permission)