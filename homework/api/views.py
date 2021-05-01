from requests import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from homework.api.serializers import FeedbackSerializer, \
    MarkHomeworkSerializer, HomeworkAnswerSerializer, \
    HomeworkSerializer
from homework.models import Feedback, MarkHomework, HomeworkAnswer, Homework


class HomeworkViewSet(ModelViewSet):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class HomeworkAnswerViewSet(ModelViewSet):
    serializer_class = HomeworkAnswerSerializer
    queryset = HomeworkAnswer.objects.all()


class MarkHomeworkViewSet(ModelViewSet):
    serializer_class = MarkHomeworkSerializer
    queryset = MarkHomework.objects.all()


class FeedbackViewSet(ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
