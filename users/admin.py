from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserForm


class CustomUserAdmin(UserAdmin):
    form = CustomUserForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'image', 'is_author', 'description')


admin.site.register(User, CustomUserAdmin)
