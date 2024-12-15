from django.db import models
from django.contrib.auth.models import User
from batch.models import Batch
from shipment.models import ShipmentDetail 
from django.urls import reverse

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    member_mapped = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    mapping_time = models.DateTimeField(auto_now_add=True)
    shipment = models.ForeignKey(ShipmentDetail, on_delete=models.CASCADE, related_name='tags')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='tags')
    emp = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emp_tags')

    def __str__(self):
        return self.tag

