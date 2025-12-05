import uuid

import pytest
from rest_framework.test import APIClient

from answers.models import Answer
from questions.models import Question


@pytest.mark.django_db
def test_create_answer_to_existing_question():
    client = APIClient()
    question = Question.objects.create(text="Test?")
    user_id = str(uuid.uuid4())

    response = client.post(
        f"/questions/{question.id}/answers/", {"user_id": user_id, "text": "Yes!"}
    )
    assert response.status_code == 201
    assert Answer.objects.filter(question=question).count() == 1
