from django.db import models
from Room.models import Room
# Create your models here.
class FeedBack(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "ID: {}|Room number : {}|created_at: {}".format(
            self.id,
            self.room.room_number,
            self.created_at
            )