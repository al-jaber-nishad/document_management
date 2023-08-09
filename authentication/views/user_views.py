from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

from authentication.models import CustomUser
from ..serializers import UserListSerializer, UserRegistrationSerializer
from ..backends import CustomUserBackend
User = get_user_model()

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # token, _ = Token.objects.get_or_create(user=user)
            response_data = serializer.data
            # response_data['token'] = token.key
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    print(CustomUser.objects.all())
    user = CustomUser.objects.get(username=username)
    print("Password match:", user)
    password_match = user.check_password(password)

    user = CustomUserBackend.authenticate(username=username, password=password)
    
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        



@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def user_detail_view(request):
    if request.method == 'GET':
        serializer = UserListSerializer(request.user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserListSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
