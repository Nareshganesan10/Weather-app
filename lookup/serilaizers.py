from rest_framework import serializers
from lookup.models import CityModel

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'