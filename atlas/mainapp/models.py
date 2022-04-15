from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DataModel(models.Model):
    sts = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    current = models.FloatField()
    def __str__(self):
        return "{}-{}".format(self.sts, self.current)

class Consumption(models.Model):
    name = models.CharField()
    current = models.FloatField()
    created_at = models.DateTimeField(verbose_name='время', auto_now_add=True)
