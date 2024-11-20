from rest_framework import serializers

from common.serializers import QuizQuestionOptionSerializer
from quiz_management.models import Quiz, QuizQuestion


class QuizQuestionMeta(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ["id", "uid", "question_text", "question_type"]


class QuizQuestionModelSerializer:
    class List(QuizQuestionMeta):
        options = QuizQuestionOptionSerializer(many=True, read_only=True)

        class Meta(QuizQuestionMeta.Meta):
            fields = QuizQuestionMeta.Meta.fields + ["options"]

    class Post(QuizQuestionMeta):
        class Meta(QuizQuestionMeta.Meta):
            fields = QuizQuestionMeta.Meta.fields
            read_only_fields = ["id", "uid"]

        def create(self, validated_data):
            request_user = self.context["request"].user
            quiz_uid = self.context["request"].parser_context["kwargs"].get("quiz_uid")
            quiz = Quiz.objects.get(uid=quiz_uid)
            if request_user.id != quiz.created_by.id:
                raise serializers.ValidationError(
                    "You are not authorized to create a question for this quiz."
                )
            validated_data["quiz"] = quiz
            return super().create(validated_data)
