from django.contrib.auth import authenticate, login

from rest_framework.decorators import  permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, LoginSerializer
from .producer import send_login_message, send_signup_message


@permission_classes([AllowAny])
class Login(APIView):

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message':"Invalid credentials"
            },status = status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=serializer.data['username'], password=serializer.data['password'])

        send_login_message({
            "user_id": user.id,
            "username": user.username,
            "status": "Logged in"
        })

        if not user:
            return Response({
                'status': False,
                'message': "credentials is Wrong"
            },status = status.HTTP_400_BAD_REQUEST)
            
        login(request, user)
        refresh = RefreshToken.for_user(user)

        return Response({
                'status': True,
                'message': 'user logged in successfully',
                'token': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                },
                'username': request.user.username,
                'user_id': user.id
            }, status = status.HTTP_200_OK)


@permission_classes([AllowAny])
class Register(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            },status = status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        send_signup_message({
            "user_id": user.id,
            "username": user.username,
        })

        return Response({
                'status': True,
                'message': 'user created successfully'
            },status = status.HTTP_201_CREATED)
    
