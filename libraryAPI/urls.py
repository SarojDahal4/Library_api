from django.urls import path
from . import views

urlpatterns = [
    
  
    path('authors/', views.AuthorListCreate.as_view(), name='authors_list'),
    path('authors/<int:pk>/', views.Authordetails.as_view(), name='authors_detail'),
    path('books/', views.BooksListCreate.as_view(), name='books_list'),
    path('books/<int:pk>/', views.Booksdetails.as_view(), name='books_detail'),  
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('test_token/', views.test_token, name='test_token'),
    
]
