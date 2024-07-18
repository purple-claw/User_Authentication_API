from rest_framework import serializers
from .models import User

# Intializing Seraliser classes to both Email and OTP for converting the data to JSON Format for API Endpoints
class UserCon(serializers.ModelSerializer):
    class Meta:
        model = User #Using User model from the previos model we crated.
        fields = ['email'] #taking the fields

#Serailser Class for OTP Generation -> JSON 
class OTPCon(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    