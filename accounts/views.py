from rest_framework import status
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from . serializer import UserSerializer , SignUpSerializer , EditProfileSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data['username']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']
    password = request.data['password']

    if not User.objects.filter(username=username).exists():
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
        )
        serializer = SignUpSerializer(user)
        json = {
            'Message':'Successfully Registered',
            'Data':serializer.data
        }
        return Response(json , status=status.HTTP_201_CREATED)
    return Response({'ERROR!!!':'User Name Already Registered'})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_info(request):
    user = User.objects.get(username = request.user)
    serializer = UserSerializer(user)
    json = {
        'Message':f'Informations Of {user} is: ',
        'data':serializer.data
    }
    return Response(json , status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def edit_profile(request):
    username = request.data['username']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    email = request.data['email']

    user = User.objects.get(username = request.user)
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()

    serializer = EditProfileSerializer(user)
    json = {
        'Message':f'Profile Of {user} Has Been Updated: ',
        'data':serializer.data
    }
    return Response(json , status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def reset_password(request):
    user = request.user
    password = request.data['password']
    confirm_password = request.data['confirm_password']

    if password == confirm_password:
        user.set_password(password)
        user.save()
        json = {
            'Done': 'Password Has Been Reseted Successfully',
            'Message':f'The New Password Is {password}'
        }
        return Response(json , status = status.HTTP_200_OK)
    return Response({'ERROR!!!':'The Password Must Be The Same Of Confirm Password'} , status = status.HTTP_400_BAD_REQUEST)