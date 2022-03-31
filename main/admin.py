from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)

class UserAdminConfig(UserAdmin):
    search_fields = ('email','username')
    list_display = ( 'username','email','is_staff','is_active')
    # fieldsets = (
    #     (None, {'fields': ('email', 'username','password','first_name','last_name')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active')}),
        
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1','password2', 'is_active', 'is_staff','first_name','last_name')}
         ),
    )
admin.site.unregister(User)
admin.site.register(User, UserAdminConfig)