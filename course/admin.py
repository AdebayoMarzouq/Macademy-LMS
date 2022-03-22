from django.contrib import admin
from .models import Course, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'tutor', 'created']
    list_filter = ['created', 'time', 'total_time']
    search_fields = ['title', 'description', 'category']
    prepopulated_fields = {'slug': ('title',)}
