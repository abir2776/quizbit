from django.db import models


class QuestionType(models.TextChoices):
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE", "Multiple Choice"
    TRUE_FALSE = "TRUE_FALSE", "True/False"
