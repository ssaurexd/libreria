#
from django.shortcuts import render
from django.db.models import Q
#
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#
from .models import Book
from .serializers import BookSerializer, PaginationBookSerializer

# Create your views here.
class BookListApiView(ListAPIView):

	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def get_queryset(self):
		return Book.objects.all() 


class BookByCategoryListApiView(ListAPIView):

	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def get_queryset(self):

		category = self.request.GET.get('category')

		return Book.objects.by_category(category)


class BookDetailApiView(RetrieveAPIView):

	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Book.objects.all()


class BookSearchApiView(ListAPIView):

	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	
	def get_queryset(self):

		libro = self.request.GET.get('title')

		queryset = Book.objects.filter(
			title__icontains=libro
		).order_by('title')

		return queryset
