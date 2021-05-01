from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from homework.services.validate import FileValidate
from user.models import Customer


class Homework(models.Model):
    who = models.ForeignKey(Customer, related_name='hw_who', on_delete=models.CASCADE)
    whom = models.ForeignKey(Customer, related_name='hw_whom', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    time_end = models.DateTimeField()


class HomeworkAnswer(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=1000, verbose_name='Comment')
    answer = models.FileField(
        upload_to='uploads/',
        validators=[FileExtensionValidator(['txt']), FileValidate.file_size]
    )


class MarkHomework(models.Model):
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE)
    mark = models.PositiveSmallIntegerField()
    who = models.ForeignKey(Customer, related_name='mark_who', on_delete=models.CASCADE)
    whom = models.ForeignKey(Customer, related_name='mark_whom', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    who = models.ForeignKey(Customer, related_name='feedback_who', on_delete=models.CASCADE)
    whom = models.ForeignKey(Customer, related_name='feedback_whom', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    homework_id = models.ForeignKey(Homework, on_delete=models.CASCADE)
    mark_id = models.ForeignKey(MarkHomework, on_delete=models.CASCADE)
