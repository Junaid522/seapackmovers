from django.contrib import admin

# Register your models here.
from container.models import MarkupKey


class MarkupKeyAdmin(admin.ModelAdmin):
    list_display = ( 'markup_key',)
    list_per_page = 25


admin.site.register(MarkupKey, MarkupKeyAdmin)