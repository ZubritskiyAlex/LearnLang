from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    time_registration = models.DateTimeField(auto_now_add=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)


