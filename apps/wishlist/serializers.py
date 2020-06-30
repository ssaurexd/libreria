from rest_framework import serializers
#
from .models import WishList
from apps.books.serializers import BookSerializer

class WishListSerializer(serializers.ModelSerializer):

	books = BookSerializer(many=True)
	
	class Meta: 
		model = WishList
		fields = (
			'books',
		)