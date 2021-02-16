from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import AdminSite
from .models import MyUser, models
from django import forms

AdminSite.site_header = "Your Name Project"

# Register your models here.
class UserAdminConfig(UserAdmin):
    ordering = ('-start_date',)
    
    list_display = ('email','first_name','last_name','gender','is_active','is_staff','is_superuser')
    
    search_fields = ('email','first_name','last_name')
    
    list_filter = ('start_date','last_login','is_active','is_staff','is_superuser')

    fieldsets = (
        (None, {'fields':('email','first_name','last_name','password')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser')}),
        ('Personal',{'fields':('gender','birth_date','start_date','last_login')})
    )
    
    readonly_fields = ('date_joined',)
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name','birth_date','gender','password1', 'password2','is_staff','is_superuser')}
        ),
    ) 

admin.site.register(MyUser, UserAdminConfig)
