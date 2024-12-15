from django.contrib import admin
from .models import Batch


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('number', 'emp', 'shipment')
    search_fields = ('number', 'emp__username', 'shipment__name')
    list_filter = ('shipment', 'emp')

