from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Page
from .forms import DefaultUserCreationForm, DefaultUserChangeForm


# class DefaultUserAdmin(UserAdmin):
#     add_form = DefaultUserCreationForm
#     form = DefaultUserChangeForm
#     model = User
#     list_display = ["username", "is_staff"]


# admin.site.register(Page, DefaultUserAdmin)
admin.site.register(Page)
