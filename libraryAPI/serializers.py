
from rest_framework import serializers
from.models import Author, Books
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        
        fields = ['name', 'birth_date', 'nationality']
        
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['name','author','publication_date','genre']
        


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email', 'password']