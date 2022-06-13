from django.contrib.auth.models import User
from django.db import models


class Value(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    values = models.ManyToManyField(Value)

    def __str__(self):
        return str(self.name)


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
