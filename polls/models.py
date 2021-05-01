from django.db import models

# Create your models here.
from user.models import Customer


class Answer(models.Model):
    answer = models.CharField(max_length=100)


class Question(models.Model):
    question = models.CharField(max_length=100, verbose_name="Question")
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number_true_answer = models.PositiveSmallIntegerField()
    answer_id = models.ManyToManyField(Answer)


class Test(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField()
    question_id = models.ManyToManyField(Question)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    theme = models.CharField(max_length=100)


class MarkPoll(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mark = models.PositiveSmallIntegerField()
    percent_mark = models.FloatField()
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
