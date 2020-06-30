#
from django.shortcuts import render
#
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
#
from .models import WishList
from .serializers import WishListSerializer

# Create your views here.
class WishListListApiView(ListAPIView):

	serializer_class = WishListSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):

		user = self.request.user

		return WishList.objects.by_user(user=user)