from django.db import models
import uuid
from django.db.models.signals import post_save, post_delete
from  django.dispatch import receiver
from author.models import Author
from user.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=250, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    sujeto = models.CharField(max_length=180, null=True)
    isbn = models.CharField(max_length=10, null=True)
    category = models.CharField(max_length=20, null=True)

def __str__(self):
        return  f"{self.name} | {self.author}"

    
class Rack(models.Model):
    rack = models.CharField(max_length=5, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recerve = models.ForeignKey(User, on_delete=models.CASCADE,
    default=None, 
    null=True, 
    blank=True,
    related_name = "recerve")
    is_reserve = models.BooleanField(default=False)
    rent = models.ForeignKey(User, on_delete=models.CASCADE,
    default=None, 
    null=True,
    blank = True,
    related_name = "rent"
    )
    is_rent = models.BooleanField(default=False, null=True)

    def __str__(self):
        return  f"{self.book.name} - {self.rack}"

 