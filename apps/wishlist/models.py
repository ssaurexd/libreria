from django.db import models
from apps.users.models import User
from apps.books.models import Book

# Create your models here.
class WishList(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	books = models.ManyToManyField(Book)

	created = models.DateField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)