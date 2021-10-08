from rest_framework import serializers

from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['author_user_id']

    def create(self, validated_data):
        project_info = Project.objects.create(**validated_data)
        project_info.author_user_id = self.context["request"].user
        project_info.save()
        Contributor.objects.create(
            user_id=self.context["request"].user,
            project_id=project_info,
            permission="Al",
            role="Author"
            )
        return project_info


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
        read_only_fields = ['project_id']


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['author_user_id', 'project_id']

    def create(self, validated_data):
        info_i = Issue.objects.create(**validated_data)
        info_i.author_user_id = self.context["request"].user
        if info_i.assignee_user_id is None:
            info_i.assignee_user_id = info_i.author_user_id
        info_i.save()
        return info_i


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author_user_id', 'issue_id']

    def create(self, validated_data):
        info_i = Comment.objects.create(**validated_data)
        info_i.author_user_id = self.context["request"].user
        info_i.save()
        return info_i