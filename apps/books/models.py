from django.db import models
from apps.categories.models import Category
from .managers import BookManager

# Create your models here.
class Book(models.Model):
	
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	price = models.FloatField()
	discount = models.FloatField()
	description = models.TextField()
	rate = models.IntegerField()
	year = models.DateField()
	editorial = models.CharField(max_length=20)
	categories = models.ManyToManyField(Category)
	image = models.ImageField(upload_to='books', null=True, blank=True)
	book_cover = models.ImageField(upload_to='books')
	in_home = models.BooleanField(default=False)

	created = models.DateField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	objects = BookManager()

	def __str__(self):
		return self.title
