from uuid import uuid4

from django.db import models


class Project(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(blank=True, null=True, default=None)
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(max_length=256)


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    picture = models.ImageField()
