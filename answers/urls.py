from django.urls import path

from . import views

urlpatterns = [
    path(
        "questions/<int:question_id>/answers/",
        views.AnswerCreateView.as_view(),
        name="answer-create",
    ),
    path("answers/<int:pk>/", views.AnswerDetailView.as_view(), name="answer-detail"),
]
