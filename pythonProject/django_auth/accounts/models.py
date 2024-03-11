from django.db import models
from django.contrib.auth.models import User

class UserChart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label1 = models.CharField(max_length=200)
    label2 = models.CharField(max_length=200)
    label3 = models.CharField(max_length=200)
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    value3 = models.IntegerField()







