from rest_framework import serializers

from polls.models import Answer, Question, Test, MarkPoll


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class MarkPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkPoll
        fields = "__all__"
