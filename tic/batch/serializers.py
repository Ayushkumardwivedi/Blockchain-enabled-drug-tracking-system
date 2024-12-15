from rest_framework import serializers
from .models import *

class UINSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
