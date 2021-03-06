from rest_framework import viewsets, permissions

from projects.permissions import ProjectPermission, IssuePermission,\
    ContributorPermission, CommentPermission
from projects.models import Project, Contributor, Issue, Comment
from projects.serializers import ProjectSerializer, ContributorSerializer,\
    IssueSerializer, CommentSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission & permissions.IsAuthenticated]
    filterset_fields = ['date', 'completed']

    def get_queryset(self, *args, **kwargs):
        contributors = Contributor.objects.filter(user_id=self.request.user)
        info_project = [contributor.project_id.id for contributor
                        in contributors]
        return Project.objects.filter(id__in=info_project)


class ContributorViewSet(viewsets.ModelViewSet):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermission & permissions.IsAuthenticated]
    filterset_fields = ['role', 'permission']

    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project_pk")
        return Contributor.objects.filter(project_id=project)

    def perform_create(self, serializer, *args, **kwargs):
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk=project_pk)
        serializer.save(project_id=project)


class IssueViewSet(viewsets.ModelViewSet):

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IssuePermission & permissions.IsAuthenticated]
    filterset_fields = ['priority', 'tag', 'status']

    def get_queryset(self, *args, **kwargs):
        project = self.kwargs.get("project_pk")
        return Issue.objects.filter(project_id=project)

    def perform_create(self, serializer, *args, **kwargs):
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk=project_pk)
        serializer.save(project_id=project)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission & permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        issue = self.kwargs.get("issue_pk")
        return Comment.objects.filter(issue_id=issue)

    def perform_create(self, serializer, *args, **kwargs):
        issue_pk = self.kwargs['issue_pk']
        issue = Issue.objects.get(pk=issue_pk)
        serializer.save(issue_id=issue)
