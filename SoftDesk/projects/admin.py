from django.contrib import admin
from .models import Project
from django.contrib import admin

from .models import Project, Contributor, Issue, Comment


# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description', 'completed')
    list_filter = ('date', 'completed')
    search_fields = ('title', )


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'role', 'permission')
    list_filter = ('role', 'permission')
    search_fields = ('role',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'tag', 'status')
    list_filter = ('priority', 'tag', 'status')
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('issue_id', 'author_user_id', 'description',
                    'created_time')
