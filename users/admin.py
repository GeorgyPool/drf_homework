from django.contrib import admin

from users.models import Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")


@admin.register(Subscription)
class AdminSubscription(admin.ModelAdmin):
    list_display = ("id", "course")
    list_filter = ("course_id",)
