from rest_framework import fields
from rest_framework.serializers import Serializer


class StandardFeedbackSerializer(Serializer):
    email = fields.EmailField()
    name = fields.CharField(max_length=25)
    message = fields.CharField(max_length=200)
