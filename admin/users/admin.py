from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'surname',
        'date_joined',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser')
    list_display_links = ('email', 'first_name', 'last_name', 'surname', )
    search_fields = ('email', 'first_name', 'last_name', 'surname')
    list_filter = ('is_active', 'is_superuser', 'is_staff')
    list_editable = ('is_active', 'is_superuser', 'is_staff')
