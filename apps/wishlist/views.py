#
from django.shortcuts import render
#
from rest_framework.generics import ListAPIView
#
from .models import WishList
from .serializers import WishListSerializer

# Create your views here.
class WishListListApiView(ListAPIView):

	serializer_class = WishListSerializer

	def get_queryset(self):
		return WishList.objects.all() 