from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.models import Account, CustomUser


class AccountInline(admin.StackedInline):
    model = Account


@admin.register(CustomUser)
class UserAdmin(ModelAdmin):
    inlines = [AccountInline]
    ordering = ["phone"]
    search_fields = ("phone",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_active",
        "role",
        "date_joined",
    )


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = (
        "user",
        "patronymic",
        "date_birth",
        "sex",
    )
