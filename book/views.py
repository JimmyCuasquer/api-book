from django.http import QueryDict
#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from book.models import Book
from book.serializers import BookItemSerializer, BookSerializer
from .premissions import IsAdmin
from rest_framework.response import Response
from  rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from book.models import Book, Rack
from user.models import User
from book.serializers import BookSerializer, BookItemSerializer, BookItemSerializerRetrieve

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class =[IsAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'author', 'category']
    
class BookItemViewset(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = BookItemSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookItemSerializerRetrieve
        else:
            return BookItemSerializer

 
    @action(detail=False)
    def list_rent_books(self, request):
       books_items = Rack.objects.filter(
            is_rent=True
        )
       serializer = BookItemSerializer(books_items, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=["patch"], detail=True)
    def set_user_rent(self, request, pk):
        rack_recerve = Rack.objects.get(pk=pk)
        print(rack_recerve.is_reserve)
        if rack_recerve.is_reserve == False or rack_recerve.is_reserve == User.objects.get(pk=request.data["rent"]): 
            rack_rent = Rack.objects.filter(rent_id= request.data["rent"]).count()
            if rack_rent >= 2:
              return Response({"message": "No puedes rentar mas de 2 libros"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(
                Rack.objects.get(pk=pk),
                data=request.data, partial=True)
            if serializer.is_valid():
                book = Rack.objects.get(pk=pk)
                book.is_rent = True
                book.save()
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Este libro esta rentado por otra persona"}, status=status.HTTP_400_BAD_REQUEST)
   
    @action(methods=["patch"], detail=True)
    def set_user_reserve(self, request, pk):
        serializer = self.serializer_class(
            Rack.objects.get(pk=pk),
            data=request.data, partial=True)
        if serializer.is_valid():
            book = Rack.objects.get(pk=pk)
            book.is_recerve = True
            book.save()
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        
