from django.db import models
from Room.models import Room
from User.models import Renter
# Create your models here.
class DailyWork(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    date = models.DateTimeField()
    task = models.CharField(max_length=255)