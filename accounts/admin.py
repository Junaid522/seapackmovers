from django.contrib import admin

# Register your models here.
from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'markup_key','created_at', 'is_active','first_name', 'last_name', 'email',)
    list_display_links = ('first_name', 'last_name', 'email',)
    search_fields = ('id', 'first_name', 'email')
    ordering = ['-id', ]


admin.site.register(User, UserAdmin)