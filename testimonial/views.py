from rest_framework import status
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from . models import Comment
from . serializer import CommentSerializer
from accounts.models import Account


@api_view(['GET' , 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments , many = True)
        json = {
            'Message':'All Comments: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        account = Account.objects.get(user = request.user)
        comment = request.data['comment']
        profession = request.data['profession']
        comment = Comment.objects.create(
            account = account,
            comment = comment,
            profession = profession,
        )
        serializer = CommentSerializer(comment)
        json = {
            'Message':'Your Comment Has Been Added: ',
            'Data':serializer.data
        }
        return Response(json , status=status.HTTP_201_CREATED)



@api_view(['GET' , 'PUT' , 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_id(request , id):
    comment_user = Comment.objects.get(id=id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment_user)
        json = {
            'Message':'Comment With This ID Is: ',
            'Data':serializer.data
        }
        return Response(json , status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        comment = request.data['comment']
        profession = request.data['profession']

        comment_user.comment = comment
        comment_user.profession = profession
        comment_user.save()

        serializer = CommentSerializer(comment_user)
        json = {
            'Message':'Your Comment Has Been Updated',
            'Data':serializer.data
        }
        return Response(json , status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        comment_user.delete()
        json = {
            'Message':'Your Comment Has Been Deleted',
        }
        return Response(json , status=status.HTTP_200_OK)



