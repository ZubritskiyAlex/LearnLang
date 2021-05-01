from django.contrib import admin

# Register your models here.
from polls.models import Question, Test, Answer, MarkPoll


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(MarkPoll)
class MarkPollAdmin(admin.ModelAdmin):
    pass
