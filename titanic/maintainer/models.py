from django.db import models

# Create your models here.
class details(models.Model):
    passengerid = models.FloatField(default=0)
    passengerclass = models.FloatField(default=0)
    age = models.FloatField(default=0)
    siblings = models.IntegerField(default=0)
    parents = models.IntegerField(default=0)
    fare = models.FloatField(default=0.00)
    female = models.IntegerField(default=0)
    male = models.IntegerField(default=0)
    c = models.IntegerField(default=0)
    q = models.IntegerField(default=0)
    s = models.IntegerField(default=0)
