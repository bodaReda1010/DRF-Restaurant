from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . models import BookTable
from . serializer import BookTableSerializer
from accounts.models import Account


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def booking(request):
    if request.method == 'GET':
        book_tables = BookTable.objects.all()
        serializer = BookTableSerializer(book_tables , many=True)
        json = {
            'Message':'All Tables: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        name_account = Account.objects.get(user = request.user)
        email = request.data['email']
        no_of_people = int(request.data['no_of_people'])
        date_and_time = request.data['date_and_time']
        if no_of_people > 0:
            table = BookTable.objects.create(
                name = name_account,
                email = email,
                no_of_people = no_of_people,
                date_and_time = date_and_time,
            )
            serializer = BookTableSerializer(table)
            json = {
                'Message':'Your Table Has Been Booked',
                'Data':serializer.data
            }
            return Response(json , status = status.HTTP_201_CREATED)
        return Response({'ERROR!!!':'Number Of People Must Be A Positive Number'} , status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def booking_id(request , id):
    table = BookTable.objects.get(id=id)
    if request.method == 'GET':
        serializer = BookTableSerializer(table)
        json = {
            'Message':'Table With This Id Is: ',
            'Data':serializer.data
        }
        return Response(json , status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        name_account = Account.objects.get(user = request.user)
        email = request.data['email']
        no_of_people = int(request.data['no_of_people'])
        date_and_time = request.data['date_and_time']
        table.name = name_account
        table.email = email
        table.no_of_people = no_of_people
        table.date_and_time = date_and_time
        if no_of_people > 0:
            table.save()
            serializer = BookTableSerializer(table)
            json = {
                'Message':'Table With This Id Has Been Updated: ',
                'Data':serializer.data
            }
            return Response(json , status = status.HTTP_202_ACCEPTED)
        return Response({'ERROR!!!':'Number Of People Must Be A Positive Number'} , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        table.delete()
        json = {
            'Message':'Table With This ID Has Been Deleted'
        }
        return Response(json , status = status.HTTP_200_OK)