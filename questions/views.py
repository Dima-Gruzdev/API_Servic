from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related("answers").all()
    serializer_class = QuestionSerializer
    http_method_names = ["get", "post", "delete"]

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Question.DoesNotExist:
            raise NotFound("Вопрос не найден")
