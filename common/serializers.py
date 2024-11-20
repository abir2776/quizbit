from rest_framework import serializers

from core.models import User
from quiz_management.models import QuestionOption, QuizQuestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone"]


class QuizQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ["id", "uid", "option_text", "is_correct_answer"]
        read_only_fields = ["id", "uid"]

    def create(self, validated_data):
        request_user = self.context["request"].user
        question_uid = (
            self.context["request"].parser_context["kwargs"].get("question_uid")
        )
        question = QuizQuestion.objects.get(uid=question_uid)
        if request_user.id != question.quiz.created_by.id:
            raise serializers.ValidationError(
                "You are not authorized to create an option for this question."
            )

        validated_data["question"] = question

        return super().create(validated_data)
