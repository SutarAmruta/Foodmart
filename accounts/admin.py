from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import User,UserProfile

# Register your models here.

class customeUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'is_active')
    odering = ('-data_joined')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, customeUserAdmin) 
admin.site.register(UserProfile) 