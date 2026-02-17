from rest_framework import serializers
from .models import Heater

class HeaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heater
        fields = '__all__'