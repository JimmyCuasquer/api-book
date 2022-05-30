from rest_framework.serializers import ModelSerializer

from user.serializers import UserSerializer
from .models import Book, Rack

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
class BookItemSerializer(ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = Rack
        fields = "__all__"

class BookItemSerializerRetrieve(ModelSerializer):
    book = BookSerializer()
    rent = UserSerializer()
    class Meta:
        model = Rack
        fields = "__all__"
      