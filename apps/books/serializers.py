#
from rest_framework import serializers, pagination
#
from apps.categories.serializers import CategorySerializer
from .models import Book

class BookSerializer(serializers.ModelSerializer):
	
	categories = CategorySerializer(many=True)

	class Meta: 
		model = Book
		fields = (
			'id',
			'title',
			'author',
			'price',
			'discount',
			'description',
			'rate',
			'year',
			'editorial',
			'image',
			'book_cover',
			'categories',
			'in_home',
		)


class PaginationBookSerializer(pagination.PageNumberPagination):
	page_size = 20
	max_page_size = 100