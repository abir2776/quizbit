from rest_framework import serializers

from common.serializers import UserSerializer
from quiz_management.models import Quiz


class QuizMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            "title",
            "start_at",
            "end_at",
        ]


class QuizModelSerializer:
    class List(QuizMetaSerializer):
        class Meta(QuizMetaSerializer.Meta):
            fields = QuizMetaSerializer.Meta.fields + ["created_by", "id", "uid"]

    class Post(QuizMetaSerializer):
        class Meta(QuizMetaSerializer.Meta):
            fields = QuizMetaSerializer.Meta.fields + ["description"]

        def create(self, validated_data):
            created_by = self.context["request"].user
            validated_data["created_by"] = created_by
            return super().create(validated_data)

    class Detail(QuizMetaSerializer):
        created_by = UserSerializer(read_only=True)

        class Meta(QuizMetaSerializer.Meta):
            fields = QuizMetaSerializer.Meta.fields + [
                "description",
                "created_by",
                "id",
                "uid",
            ]

    class Update(QuizMetaSerializer):
        class Meta(QuizMetaSerializer.Meta):
            fields = QuizMetaSerializer.Meta.fields + ["description"]
