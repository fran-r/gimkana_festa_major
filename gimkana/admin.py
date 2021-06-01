from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Qr, UserQr


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)

    ordering = ('-date_joined',)


class QrAdmin(admin.ModelAdmin):
    list_display = ('num_order', 'title', 'is_shop', 'value', 'is_available',)
    list_filter = ('is_shop', 'value', 'is_available',)


class UserQrAdmin(admin.ModelAdmin):
    list_display = ('qr', 'user', 'scan_date', 'hints', 'value')
    list_filter = ('qr', 'user', 'scan_date', 'hints',)

    fieldsets = (
        (None, {
            'fields': ('qr', 'user')
        }),
        ('Availability', {
            'fields': ('hints', 'scan_date')
        }),
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Qr, QrAdmin)
admin.site.register(UserQr, UserQrAdmin)
