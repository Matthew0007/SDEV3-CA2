
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser 

#superuserlogin : superuser, password:easypass

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser #new
    list_display = ['email', 'username', 'age', 'is_staff', ] #new

admin.site.register(CustomUser, CustomUserAdmin)