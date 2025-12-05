from rest_framework import serializers

from answers.serializers import AnswerSerializer

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "created_at", "answers"]
        read_only_fields = ["id", "created_at"]
