from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    

class LogoutView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated)
    