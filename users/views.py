from django.shortcuts import render
from .serializers import CustomTokenObtainPairSerializer, UserSerializer, UserRegisterSerializer, LoginSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)