from django.db import models
from django.contrib.auth.models import User

from shipment.models import ShipmentDetail 

class Batch(models.Model):
    number = models.CharField(max_length=100)
    emp = models.ForeignKey(User, on_delete=models.CASCADE, related_name='batch_emps')
    shipment = models.ForeignKey(ShipmentDetail, on_delete=models.CASCADE,related_name='batch_shipments')
    
    def __str__(self):
        return self.number
