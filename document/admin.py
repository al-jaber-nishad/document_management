from django.contrib import admin

from .models import *


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Document._meta.fields]
