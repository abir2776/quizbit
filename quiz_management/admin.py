from django.contrib import admin

from quiz_management.models import *

admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizParticipant)
admin.site.register(QuestionOption)
admin.site.register(ParticipantAnswer)
