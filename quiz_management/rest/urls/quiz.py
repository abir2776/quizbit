from django.urls import path

from ..views.quiz import QuizDetailAPIView, QuizListCreateAPIView
from ..views.quiz_participant import (
    QuizParticipantDetailAPIView,
    QuizParticipantListCreateAPIView,
)
from ..views.quiz_question import (
    QuizQuestionListCreateAPIView,
    QuizQuestionOptionListCreateAPIView,
    submit_question_answer,
)

urlpatterns = [
    path("", QuizListCreateAPIView.as_view(), name="quiz-list-create"),
    path("/<uuid:uid>", QuizDetailAPIView.as_view(), name="quiz-detail"),
    path(
        "/<uuid:quiz_uid>/participants",
        QuizParticipantListCreateAPIView.as_view(),
        name="quiz-participant-list-create",
    ),
    path(
        "/<uuid:quiz_uid>/participants/<uuid:uid>",
        QuizParticipantDetailAPIView.as_view(),
        name="quiz-participant-detail",
    ),
    path(
        "/<uuid:quiz_uid>/questions",
        QuizQuestionListCreateAPIView.as_view(),
        name="quiz-questions",
    ),
    path(
        "/<uuid:quiz_uid>/questions/<uuid:question_uid>/options",
        QuizQuestionOptionListCreateAPIView.as_view(),
        name="quiz-question-options",
    ),
    path(
        "/<uuid:quiz_uid>/questions/<uuid:question_uid>/options/<uuid:option_uid>/select",
        submit_question_answer,
        name="submit_question_answer",
    ),
]
