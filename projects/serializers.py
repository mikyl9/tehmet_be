from rest_framework import fields, serializers

from projects.models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ("id", "image")


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ("id", "name", "title", "logo", "images", "description", "is_active", "created_at")
