from django.contrib import admin
from .models import Question, QuestionTag


# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionTag)