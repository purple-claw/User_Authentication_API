from django.shortcuts import render
import random
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .controller import UserCon, OTPCon


#Creating a Post Handler for API Endpoint /api/register
class RegPoint(APIView):
    def post(self,request):
        temp = UserCon(data=request.data)
        if temp.is_valid():
            temp.save()
            return Response({ 'message' : 'Dear user, the Registration is Succesful. Now you can Verify Your OTP to continue using our Services!!!!'}, status=status.HTTP_201_CREATED)
        return Response(temp.errors, status=status.HTTP_400_BAD_REQUEST)

#Creating a Post Handler for API Endpoint /api/request-otp
class OTPRequest(APIView):
    def post(self,request):
        email=request.data.get('email')
        if email:
            user, created = User.objects.get_or_create(email=email)
            otp = random.randint(100000,999999)
            user.otp = str(otp)
            user.otp_gen_time = timezone.now()
            user.save()
            send_mail('Dear User',f'Your OTP for Verification is {otp}', 'from@UniAcco.com', [email])
            return Response({'message':'OTP for Verification is Sent to your Email'}, status=status.HTTP_200_OK)
        return Response({'Error!':'Invalid Email Passed'}, status=status.HTTP_401_UNAUTHORIZED)

#Creating a Post Handler for API Endpoint /api/verify-otp
class OTPVerify(APIView):
    def post(self, request):
        serializer = OTPCon(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            user = User.objects.filter(email=email).first()
            if user and user.otp == otp and user.otp_gen_time > timezone.now() - timedelta(minutes=5):
                refresh = RefreshToken.for_user(user)
                return Response({'message': 'Login successful.', 'token': str(refresh.access_token)}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid OTP or OTP expired.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
