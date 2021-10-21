from rest_framework import permissions
from .models import Contributor


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        try:
            info_contributor = Contributor.objects.get(
                user_id=request.user, project_id=obj
                )
        except Contributor.DoesNotExist:
            return False

        if info_contributor.permission == "Al":
            return True
        elif info_contributor.permission == "Rd":
            return request.method in permissions.SAFE_METHODS


class ContributorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        id_project = view.kwargs.get("project_pk")
        try:
            info_contributor = Contributor.objects.get(
                user_id=request.user, project_id=id_project
                )
        except Contributor.DoesNotExist:
            return False
        if info_contributor.permission in ["Al", "Rd"]:
            return True

    def has_object_permission(self, request, view, obj):
        id_project = view.kwargs.get("project_pk")
        try:
            info_contributor = Contributor.objects.get(
                user_id=request.user, project_id=id_project
                )
        except Contributor.DoesNotExist:
            return False
        if info_contributor.permission == "Al":
            return request.method in ["DELETE"]
        elif info_contributor.permission == "Rd":
            if request.user == obj.user_id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS


class IssuePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        id_project = view.kwargs.get("project_pk")
        try:
            info_contributor = Contributor.objects.get(
                user_id=request.user, project_id=id_project)
        except Contributor.DoesNotExist:
            return False
        if info_contributor.permission in ["Al", "Rd"]:
            return True

    def has_object_permission(self, request, view, obj):
        id_project = view.kwargs.get("project_pk")
        try:
            info_contributor = Contributor.objects.get(
                user_id=request.user, project_id=id_project
                )
        except Contributor.DoesNotExist:
            return False
        if info_contributor.permission == "Al":
            return True
        elif info_contributor.permission == "Rd":
            if request.user == obj.author_user_id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS


class CommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        id_project = view.kwargs.get("project_pk")
        try:
            info_contributor = Contributor.objects.get(
                user_id=request.user, project_id=id_project
                )
        except Contributor.DoesNotExist:
            return False
        if info_contributor.permission in ["Al", "Rd"]:
            return True

    def has_object_permission(self, request, view, obj):
        id_project = view.kwargs.get("project_pk")
        try:
            info_contributor = Contributor.objects.get(
                user_id=request.user, project_id=id_project
                )
        except Contributor.DoesNotExist:
            return False
        if info_contributor.permission == "Al":
            return True
        elif info_contributor.permission == "Rd":
            if request.user == obj.author_user_id:
                return True
            else:
                return request.method in permissions.SAFE_METHODS
