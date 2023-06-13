from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin



class ProfileInline(admin.TabularInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', )

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('username', 'email', 'first_name', 'last_name', )
    ordering = ('last_name', 'first_name', )

    inlines = [ProfileInline, ]

