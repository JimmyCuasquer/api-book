from django.shortcuts import render
from rest_framework.response import Response

import author
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from  rest_framework import status
from .permissions import OnlyAdmin
from rest_framework.decorators import action
from book.models import Book,Rack
from book.serializers import BookSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  User.objects.all()
    permission_classes =[OnlyAdmin]

    @action(detail =True)
    def my_rent_book(self, request, pk):
        books = Rack.objects.filter(
            rent_id=pk
        )
        try:
            serializer = BookSerializer(books, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True)
    def my_reserve_books(self,request, pk):

        books = Rack.objects.filter(
            recerve_id=pk
        )
        serializer = BookSerializer(books, many=True)
        try:
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
