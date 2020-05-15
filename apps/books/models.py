from django.db import models
from apps.categories.models import Category

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
	image = models.ImageField(upload_to='books')
	book_cover = models.ImageField(upload_to='books')

	created = models.DateField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title
