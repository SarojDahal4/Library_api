from tkinter import CASCADE
from typing import Self
from django.db import models

# Create your models here.

    
    
class Author(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Books(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    publication_date = models.DateField()
    genre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        