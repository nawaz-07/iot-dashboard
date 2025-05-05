from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get("password")
    confirm_password = request.data.get("confirm_password")

    if not username and not not password and not confirm_password:
        return Response({"error":"Username and Password required"}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({"Error":"User Already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    if password != confirm_password:
        return Response({"Error":"Password and Confirm Password are not same"})
    
    user = User.objects.create_superuser(username=username, password=password)
    token = Token.objects.create(user=user)
    
    return Response({"message":"User Created","token": token.key}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username and not password:
        return Response({"Error":"username and password required"}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)

    if not user:
        return Response({"error":"Invalid user credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    token,_= Token.objects.get_or_create(user=user)
    return Response({'massage':"login seccessfully", "token":token.key})