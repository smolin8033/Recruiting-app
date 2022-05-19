from django.contrib.auth.models import User
from django.db import models


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    candidate = models.ForeignKey(Candidate, related_name='tags', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Value(models.Model):
    name = models.CharField(max_length=50)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, related_name='values', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
