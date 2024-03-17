from django.core.exceptions import PermissionDenied
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DeleteView


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,blank=False,null=False)
    value = models.FloatField()

    def __str__(self):
        return f'{self.company_name} - {self.value}'


