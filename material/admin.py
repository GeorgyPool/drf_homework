from django.contrib import admin

from material.models import Course, Lesson


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Lesson)
class AdminLessons(admin.ModelAdmin):
    list_display = ("id", "title")
    list_filter = ("course_id",)
