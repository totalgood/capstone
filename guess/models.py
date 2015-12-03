from django.db import models
from django.contrib.postgres.fields import ArrayField


class Drawing(models.Model):

    values_array = ArrayField(models.FloatField(default=0.0))
    guess = models.IntegerField(default=None)
    confidence = models.FloatField(default=None)
    tiny_array = ArrayField(models.FloatField(default=0.0), default=[])
    correct = models.BooleanField(default=True)