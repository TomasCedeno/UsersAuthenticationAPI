from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

from .rol import Rol

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un usuario.
        """
        if not email:
            raise ValueError('User must have an email')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField('User Email', max_length = 100, unique=True)
    password = models.CharField('User Password', max_length = 256)
    name = models.CharField('User Name', max_length = 30)
    lastName = models.CharField('User LastName', max_length = 30)
    roles = models.ManyToManyField(Rol)


    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'email' #Indica que se quiere hacer login con 'email' y no con 'username'