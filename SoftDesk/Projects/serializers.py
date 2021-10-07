from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'date', 'description', 'type', 'completed',
                  'author_user_id']
        read_only_fields = ['author_user_id']

    def create(self, validated_data):
        project_info = Project.objects.create(**validated_data)
        project_info.author_user_id = self.context["request"].user
        project_info.save()
        return project_info
