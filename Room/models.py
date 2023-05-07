from django.db import models

# Create your models here.
class Room(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(room_number__gte = 0,area__gte = 0,
                                                  room_price__gte = 0), name ='gte 0'),
        ]
    
    room_id = models.CharField(max_length=20, primary_key=True)
    room_number = models.IntegerField(unique=True)
    area = models.CharField(max_length=20)
    room_price = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=250, default='')

    def __str__(self):
        return "room number : "+ str(self.room_number)