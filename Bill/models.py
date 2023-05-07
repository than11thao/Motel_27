from django.db import models
from Room.models import Room
import datetime
# Create your models here.

class Bill(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    cubic_metres_of_water = models.FloatField()
    water_price = models.FloatField()
    electrict_number = models.FloatField()
    electricity_price = models.FloatField()
    discount = models.IntegerField(default=0)
    date = models.DateField()
    pay_status = models.BooleanField(default=False)

    def get_total(self):
        return (self.cubic_metres_of_water*self.water_price + self.electricity_price*self.electrict_number + self.room.room_price)
    
    def get_total_amount(self):
        return ((self.cubic_metres_of_water*self.water_price + self.electricity_price*self.electrict_number + self.room.room_price)
                *(100-self.discount))/100
    
    def __str__(self):
        print(dir(self.date))
        print(self.date)
        return "Room: {}- Date : {}-{}-{}- Total amount: {}VND".format(self.room, self.date.day,self.date.month,self.date.year,
                                                   self.get_total_amount()
                                                   )
    