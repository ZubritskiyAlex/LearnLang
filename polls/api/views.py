
from rest_framework.viewsets import ModelViewSet

from polls.api.serializers import AnswerSerializer, QuestionSerializer, TestSerializer, MarkPollSerializer
from polls.models import Answer, Question, Test, MarkPoll


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class TestViewSet(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class MarkPollViewSet(ModelViewSet):
    serializer_class = MarkPollSerializer
    queryset = MarkPoll.objects.all()
