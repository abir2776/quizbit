from rest_framework import serializers

from common.serializers import UserSerializer
from quiz_management.models import Quiz, QuizParticipant


class QuizParticipantMeta(serializers.ModelSerializer):
    class Meta:
        model = QuizParticipant
        fields = []


class QuizParticipantModelSerializer:
    class List(QuizParticipantMeta):
        user = UserSerializer(read_only=True)

        class Meta(QuizParticipantMeta.Meta):
            fields = QuizParticipantMeta.Meta.fields + [
                "score",
                "user",
                "started_at",
                "finished_at",
                "id",
                "uid",
                "num_of_correct_answer",
                "num_of_wrong_answer",
            ]

    class Post(QuizParticipantMeta):
        class Meta(QuizParticipantMeta.Meta):
            fields = []

        def create(self, validated_data):
            user = self.context["request"].user
            quiz_uid = self.context["request"].parser_context["kwargs"].get("quiz_uid")
            quiz = Quiz.objects.get(uid=quiz_uid)
            return QuizParticipant.objects.create(quiz=quiz, user=user)

    class Detail(QuizParticipantMeta):
        user = UserSerializer(read_only=True)

        class Meta(QuizParticipantMeta.Meta):
            fields = QuizParticipantMeta.Meta.fields + [
                "score",
                "user",
                "started_at",
                "finished_at",
                "id",
                "uid",
                "num_of_correct_answer",
                "num_of_wrong_answer",
            ]
