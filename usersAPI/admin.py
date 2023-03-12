from django.contrib import admin

from .models.user import User
from .models.rol import Rol
from .models.permission import Permission

admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Permission)