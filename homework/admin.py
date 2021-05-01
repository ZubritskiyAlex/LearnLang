from django.contrib import admin

from homework.models import Homework, HomeworkAnswer, MarkHomework, Feedback


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    pass


@admin.register(HomeworkAnswer)
class HomeworkAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(MarkHomework)
class MarkHomeworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass