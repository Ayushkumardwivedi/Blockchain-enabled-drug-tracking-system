from django.db import models
from django.contrib.auth.models import User

class ShipmentDetail(models.Model):
    shipment = models.CharField(max_length=100)
    # shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE, primary_key=True, related_name='shipment_detail')
    start = models.DateTimeField()
    end = models.DateTimeField()
    batches = models.CharField(max_length=100)
    truck = models.CharField(max_length=100)
    emp = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shipment_batches')

    def __str__(self):
        return f"Shipment {self.shipment}"