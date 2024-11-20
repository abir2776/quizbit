from rest_framework import generics

from quiz_management.models import QuizParticipant

from ..serializers.quiz_participant import QuizParticipantModelSerializer


class QuizParticipantListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = QuizParticipantModelSerializer.List

    def get_serializer_class(self):
        if self.request.method == "POST":
            return QuizParticipantModelSerializer.Post
        return QuizParticipantModelSerializer.List

    def get_queryset(self):
        return QuizParticipant.objects.filter(quiz__uid=self.kwargs.get("quiz_uid"))


class QuizParticipantDetailAPIView(generics.RetrieveAPIView):
    queryset = QuizParticipant.objects.all()

    serializer_class = QuizParticipantModelSerializer.Detail

    def get_object(self):
        quiz_uid = self.kwargs.get("quiz_uid")
        uid = self.kwargs.get("uid")
        return generics.get_object_or_404(
            QuizParticipant.objects.filter(), uid=uid, quiz__uid=quiz_uid
        )
