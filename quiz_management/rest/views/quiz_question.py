from rest_framework import generics, response, status
from rest_framework.decorators import api_view

from common.serializers import QuizQuestionOptionSerializer
from quiz_management.models import (
    ParticipantAnswer,
    QuestionOption,
    QuizParticipant,
    QuizQuestion,
)

from ..serializers.quiz_question import QuizQuestionModelSerializer


class QuizQuestionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = QuizQuestionModelSerializer.List

    def get_serializer_class(self):
        if self.request.method == "POST":
            return QuizQuestionModelSerializer.Post
        return QuizQuestionModelSerializer.List

    def get_queryset(self):
        return QuizQuestion.objects.prefetch_related("options").filter(
            quiz__uid=self.kwargs.get("quiz_uid")
        )


class QuizQuestionOptionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = QuizQuestionOptionSerializer

    def get_queryset(self):
        question_uid = self.kwargs.get("question_uid")
        return QuestionOption.objects.filter(question__uid=question_uid)


@api_view(["POST"])
def submit_question_answer(request, quiz_uid, question_uid, option_uid):
    is_registered = QuizParticipant.objects.filter(
        user=request.user, quiz__uid=quiz_uid
    )
    if not is_registered.exists():
        return response.Response(
            {"error": "You are not registered for this quiz."},
            status=status.HTTP_403_FORBIDDEN,
        )

    prev_answer = ParticipantAnswer.objects.filter(
        question__uid=question_uid, participant=is_registered.first()
    )
    if prev_answer.exists():
        new_option = generics.get_object_or_404(
            QuestionOption.objects.filter(), uid=option_uid
        )
        prev_answer.option = new_option
        prev_answer.save()

    return response.Response({"success"}, status=status.HTTP_200_OK)
