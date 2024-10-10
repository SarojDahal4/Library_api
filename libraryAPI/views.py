import token
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response  import Response
from rest_framework import generics, status, serializers
from rest_framework.decorators import  api_view, authentication_classes, permission_classes
from.models import Author, Books
from .serializers import AuthorSerializer, BooksSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

# create you view using app view
@api_view(['POST'])
def book(request):
    serializers = BooksSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def book_detail(request):
    objs = Books.objects.get.all()
    serializers = BooksSerializer.objects(objs, many=True)
    return Response(serializers.data)

@api_view(['PUT','PATCH'])
def book_update(request):
    data = request.data
    if request.method == 'PUT':
        serializers = BooksSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        data = request.data
        serializers = BooksSerializer(data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE '])
def book_delete(request):
    data = request.data
    ojs = Books.objects.get(id=data['id'])
    ojs.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# created using viewset

   
   
# class BooksListCreate(generics.ListCreateAPIView):
   
#    queryset = Books.objects.all()
#    serializer_class = BooksSerializer
    

# class Booksdetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer
    
# class AuthorListCreate(generics.ListCreateAPIView):
#    queryset = Author.objects.all()
#    serializer_class = AuthorSerializer
    
    
# class Authordetails(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Author.objects.all()
#    serializer_class = AuthorSerializer
    
    
# authentication  


@api_view(['POST'])
def login(request):
   # requesting a data and password also storing it in variables
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'detail': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    if not user.check_password(password):
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    
    return Response({'token': token.key, 'user': serializer.data})


@api_view(['POST'])
def signup(request):
    data = request.data
    serializers = UserSerializer(data=data)
    if serializers.is_valid():
        serializers.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response ({'token':token.key,"user": serializers.data})
        
    
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 




@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({'detail': 'You are authenticated'})
    