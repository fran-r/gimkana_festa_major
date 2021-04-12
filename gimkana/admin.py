from django.contrib import admin

from .models import Qr, QrScan

admin.site.register(Qr)

@admin.register(QrScan)
class QrScanAdmin(admin.ModelAdmin):
    list_display = ('qr', 'status', 'scanned_by', 'scan_date')
    list_filter = ('status', 'scan_date')

    fieldsets = (
        (None, {
            'fields': ('id', 'qr', 'scanned_by')
        }),
        ('Availability', {
            'fields': ('status', 'scan_date')
        }),
    )
