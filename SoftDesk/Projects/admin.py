from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description', 'completed')
    list_filter = ('date', 'completed')
    search_fields = ('title', )
