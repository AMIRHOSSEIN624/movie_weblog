from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserCreationForm
    add_form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),

    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),

    )


admin.site.register(CustomUser, CustomAdmin)
