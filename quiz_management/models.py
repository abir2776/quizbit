from django.db import models

from common.models import BaseModelWithUID

from .choices import QuestionType


class Quiz(BaseModelWithUID):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_by = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="created_quizzes"
    )

    def __str__(self):
        return f"{self.title} (ID: {self.uid})"


class QuizParticipant(BaseModelWithUID):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="participants"
    )
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    score = models.IntegerField(default=-1)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    num_of_correct_answer = models.IntegerField(null=True, blank=True)
    num_of_wrong_answer = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.quiz.title} - {self.user.first_name} (ID: {self.uid})"


class QuizQuestion(BaseModelWithUID):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(
        max_length=20,
        choices=QuestionType.choices,
        default=QuestionType.MULTIPLE_CHOICE,
    )

    def __str__(self):
        return f"{self.question_text} (ID: {self.uid})"


class QuestionOption(BaseModelWithUID):
    question = models.ForeignKey(
        QuizQuestion, on_delete=models.CASCADE, related_name="options"
    )
    option_text = models.CharField(max_length=200)
    is_correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.option_text} (ID: {self.uid})"


class ParticipantAnswer(BaseModelWithUID):
    participant = models.ForeignKey(
        QuizParticipant, on_delete=models.CASCADE, related_name="answers"
    )
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participant.quiz.title} - {self.participant.user.first_name} (ID: {self.uid})"
