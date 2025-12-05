from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.models import Question

from .models import Answer
from .serializers import AnswerSerializer


class AnswerCreateView(APIView):
    def post(self, request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            return Response(
                {"error": "Вопрос не найден"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(question=question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetailView(APIView):
    def get(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise NotFound("Ответ не найден")
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            answer = Answer.objects.get(pk=pk)
            answer.delete()
            return Response({"ok": True}, status=status.HTTP_200_OK)
        except Answer.DoesNotExist:
            raise NotFound("Ответ не найден")
