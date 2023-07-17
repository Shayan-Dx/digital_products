from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import User


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields' : ('username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'phone_number', 'email')}),
        (_('Permisssions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('username', 'phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'username', 'phone_number', 'email', 'is_staff')
    search_fields = ['username__exact']
    ordering = ('-id',)

admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)