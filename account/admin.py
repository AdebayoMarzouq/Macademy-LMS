from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_filter = ('email', 'is_tutor', 'is_active')
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_tutor', 'age']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('is_tutor', 'age')}
         ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('is_tutor', 'age')}
         ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'phone_no', 'country']
    list_filter = ('gender', 'country')
