from uuid import uuid4

from django.db import models


class Project(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    logo = models.ImageField(upload_to="projects/logos", blank=True, null=True, default=None)
    description = models.TextField(max_length=256)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} {self.title}"


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/images")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
