from django.db import models
from django.contrib.auth.models import User



class DataModel(models.Model):
    sts = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    current = models.FloatField()
    category_name = models.CharField(max_length=200,default='user_table')

    def __str__(self):
        return "{}-{}".format(self.sts, self.current)

