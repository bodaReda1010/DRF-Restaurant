from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . models import Chef
from . serializer import ChefSerializer



@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def team(request):
    if request.method == 'GET':
        chefs = Chef.objects.all()
        serializer = ChefSerializer(chefs , many=True)
        json = {
            'Message':'All Team: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ChefSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            json = {
                'Message':'One Chef Has Been Added To Team: ',
                'Data':serializer.data
            }
            return Response(json , status=status.HTTP_201_CREATED)
        json = {
            'ERROR!!!':'Invalid , Please Enter A Name And Job Title',
        }
        return Response(json , status = status.HTTP_400_BAD_REQUEST)




@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def team_id(request , id):
    chef = Chef.objects.get(id=id)
    if request.method == 'GET':
        serializer = ChefSerializer(chef)
        json = {
            'Message':'Chef With This Id Is: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ChefSerializer(chef , data = request.data)
        if serializer.is_valid():
            serializer.save()
            json = {
            'Message':'Data With This Chef Has Been Updated: ',
            'Data':serializer.data
            }
            return Response(json , status = status.HTTP_202_ACCEPTED)
        json = {
            'ERROR!!!':'Invalid , Please Enter A Name And Job Title',
        }
        return Response(json , status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        chef.delete()
        json = {
            'Message':'Chef Wit This ID Has Been Deleted'
        }
        return Response(json , status = status.HTTP_200_OK)