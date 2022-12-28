from django.db import models

class Familiares(models.Model):
    name = models.CharField(max_length=100)
    age = models.FloatField()
    alive = models.BooleanField()
















