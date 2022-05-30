from rest_framework import viewsets
from .models import Author
from author.serializers import AuthorSerializer

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset =  Author.objects.all()
  