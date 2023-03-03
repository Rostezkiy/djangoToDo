from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)


class Task(models.Model):
    parent_list = models.ForeignKey(List,
                                    on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False,
                                    blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
