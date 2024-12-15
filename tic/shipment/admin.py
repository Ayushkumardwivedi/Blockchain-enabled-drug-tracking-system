from django.contrib import admin
from .models import ShipmentDetail

@admin.register(ShipmentDetail)
class ShipmentDetailAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'start', 'end', 'truck', 'emp')
    search_fields = ('shipment__name', 'truck', 'emp__username')
    list_filter = ('start', 'end', 'shipment')
