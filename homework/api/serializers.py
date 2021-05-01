from rest_framework import serializers

from homework.models import Homework, HomeworkAnswer, Feedback, MarkHomework


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class HomeworkAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkAnswer
        fields = "__all__"


class MarkHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkHomework
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
