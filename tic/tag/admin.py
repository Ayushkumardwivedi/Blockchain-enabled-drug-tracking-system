from django.contrib import admin
from .models import Tag  
from django.utils.html import format_html, mark_safe
from django.shortcuts import render

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'location', 'member_mapped', 'mapping_time', 'shipment', 'batch', 'emp')

admin.site.register(Tag, TagAdmin)

