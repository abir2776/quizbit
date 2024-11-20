from rest_framework import generics

from quiz_management.models import Quiz

from ..serializers.quiz_serializers import QuizModelSerializer


class QuizListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizModelSerializer.List

    def get_serializer_class(self):
        if self.request.method == "POST":
            return QuizModelSerializer.Post
        return QuizModelSerializer.List


class QuizDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizModelSerializer.Detail

    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return QuizModelSerializer.Update
        return QuizModelSerializer.Detail
