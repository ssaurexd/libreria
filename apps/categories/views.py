#
from django.shortcuts import render
#
from rest_framework.generics import ListAPIView
#
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryListApiView(ListAPIView):

	serializer_class = CategorySerializer

	def get_queryset(self):
		return Category.objects.all() 