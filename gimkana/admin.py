from django.contrib import admin

from .models import Qr, UserQr

admin.site.register(Qr)


@admin.register(UserQr)
class QrScanAdmin(admin.ModelAdmin):
    list_display = ('qr', 'user', 'hints', 'scan_date')
    list_filter = ('hints', 'scan_date')

    fieldsets = (
        (None, {
            'fields': ('id', 'qr', 'user')
        }),
        ('Availability', {
            'fields': ('hints', 'scan_date')
        }),
    )
