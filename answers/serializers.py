from rest_framework import serializers

from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question_id", "user_id", "text", "created_at"]
        read_only_fields = ["id", "created_at"]
