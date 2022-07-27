from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User


class UserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'name', 'email', 'user_type')
    list_filter = ('is_staff',)
    fieldsets = (
        ('Personal info', {'fields': ('name', 'user_type', 'email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'user_type', 'is_active', 'is_staff', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('id',)


admin.site.register(User, UserAdmin)
