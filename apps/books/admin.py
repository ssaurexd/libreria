from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	'''Admin View for Book'''

	list_display = (
		'id',
		'title',
		'author',
		'in_home',
		'price',
		'discount',
		'year',
		'editorial',
		'rate',
		'image',
		'book_cover',
	)