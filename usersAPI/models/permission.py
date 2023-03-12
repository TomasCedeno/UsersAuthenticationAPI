from django.db import models

class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Permission Name', max_length=30, unique=True)