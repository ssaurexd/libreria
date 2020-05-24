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

	def get_queryset(self):
		return Book.objects.all() 


class BookByCategoryListApiView(ListAPIView):

	serializer_class = BookSerializer

	def get_queryset(self):

		category = self.request.GET.get('category')

		return Book.objects.by_category(category)


class BookDetailApiView(RetrieveAPIView):

	serializer_class = BookSerializer
	
	def get_queryset(self):

		pk = self.kwargs['pk']

		return Book.objects.filter(id=pk)
	