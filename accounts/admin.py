from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class GimkanaUserAdmin(UserAdmin):
    pass


admin.site.register(User, GimkanaUserAdmin)
