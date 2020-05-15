#
from django.shortcuts import render
#
from rest_framework.generics import ListAPIView, RetrieveAPIView
#
from .models import Book
from .serializers import BookSerializer, PaginationBookSerializer

# Create your views here.
class BookListApiView(ListAPIView):

	serializer_class = BookSerializer
	pagination_class = PaginationBookSerializer

	def get_queryset(self):
		return Book.objects.all() 


class BookDetailApiView(RetrieveAPIView):

	serializer_class = BookSerializer
	
	def get_queryset(self):

		pk = self.kwargs['pk']

		return Book.objects.filter(id=pk)
	