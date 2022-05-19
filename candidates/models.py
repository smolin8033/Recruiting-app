from django.contrib.auth.models import User
from django.db import models


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class Value(models.Model):
    name = models.CharField(max_length=50)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
