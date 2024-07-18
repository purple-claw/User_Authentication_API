from django.urls import path
from .views import RegPoint, OTPRequest, OTPVerify

urlpatterns = [
    path('register', RegPoint.as_view(), name='register'),
    path('request-otp', OTPRequest.as_view(), name='request-otp'),
    path('verify-otp', OTPVerify.as_view(), name='verify-otp'),
]
