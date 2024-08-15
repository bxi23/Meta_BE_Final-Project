from django.contrib.auth.models import User
from .models import menu, booking
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'